import unittest
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
    extract_markdown_links,
    extract_markdown_images,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_bolded_word(self):
        input_nodes = [ TextNode("Code is 'code' or is it", "text")]
        expected_output = [
            TextNode("Code is ", "text"),
            TextNode("code", "code"),
            TextNode(" or is it", "text"),
            ]
        output = split_nodes_delimiter(input_nodes, "'", "code")
        assert output == expected_output, "Basic splitting does not work as expected."

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_markdown_test(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        )
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("another", "https://i.imgur.com/dfsdkjfd.png"),
            ],
            matches,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
        )
   

    def test_link_node(self):
        input_text = "[boot.dev](https://boot.dev)"
        expected_output = [
            TextNode("boot.dev", text_type_link, "https://boot.dev")
        ]
        assert text_to_textnodes(input_text) == expected_output


    def test_image_node(self):
        input_text = "![image](https://example.com/image.png)"
        expected_output = [
            TextNode("image", text_type_image, "https://example.com/image.png")
        ]
        assert text_to_textnodes(input_text) == expected_output

    def test_combined_styles(self):
        input_text = "This is **bold**, *italic*, and `code`."
    

    def test_text_to_textnodes_complex(self):
        input_text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected_output = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev")
        ]
        assert text_to_textnodes(input_text) == expected_output




if __name__ == "__main__":
    unittest.main()
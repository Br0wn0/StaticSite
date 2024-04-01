import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_olist,
    block_type_ulist,
    block_type_quote,
    heading_to_html,
    ordered_list_to_html,
)

def test_markdown():
    markdown = '''safesfsd dsfsfsdf             
    dsadasdaddsafsweasfefew 
    
    wefwefwef '''
    mk = markdown_to_blocks(markdown)
    print(mk)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_markdown_to_blocks_splits_correctly(self):
    # Test case with paragraphs
        markdown = "This is a test\n\nThis is another test"
        expected_blocks = ["This is a test", "This is another test"]
        assert markdown_to_blocks(markdown) == expected_blocks, "Failed to split paragraphs"
    
        # Test case with mixed content
        markdown = "# Heading\n\n* List item 1\n* List item 2"
        expected_blocks = ["# Heading", "* List item 1\n* List item 2"]
        assert markdown_to_blocks(markdown) == expected_blocks, "Failed to handle mixed content"



    def test_block_to_block_type_identifies_types_correctly(self):
    # Test case for heading
        heading = "# This is a heading"
        assert block_to_block_type(heading) == block_type_heading, "Failed to identify heading"
    
    # Test case for ordered list
        ordered_list = "1. First item\n2. Second item"
        assert block_to_block_type(ordered_list) == block_type_olist, "Failed to identify ordered list"
    
    # Test case for code block
        code_block = "```python\nprint('Hello')\n```"
        assert block_to_block_type(code_block) == block_type_code, "Failed to identify code block"



    def test_heading_to_html_converts_correctly(self):
    # Test case for an h1 heading
        h1_heading = "# This is an H1"
        print(heading_to_html(h1_heading))
        # Assuming ParentNode has a method to_html() that returns the HTML as a string
        result_node = heading_to_html(h1_heading)
        assert result_node.to_html() == "<h1>This is an H1</h1>", "Failed to convert H1 heading"
    # Test case for an h2 heading
        h2_heading = "## This is an H2"
        # Assuming h2_heading is properly defined earlier
        result_node = heading_to_html(h2_heading)
        assert result_node.to_html() == "<h2>This is an H2</h2>", "Failed to convert H2 heading"

    # Test case for incorrect heading with no space
        no_space_heading = "#This is not correctly formatted"
        assert heading_to_html(no_space_heading) != "<h1>This is not correctly formatted</h1>", "Incorrectly handled heading with no space"


    class TestOrderedListToHtml(unittest.TestCase):
        def test_ordered_list_to_html_converts_correctly(self):
        # Define a simple input ordered list
            simple_olist = "1. First item\n2. Second item\n3. Third item"

        # Define the expected HTML output
            expected_html = "<ol><li>First item</li><li>Second item</li><li>Third item</li></ol>"

        # Call the function and check the output
            actual_html = ordered_list_to_html(simple_olist)
            self.assertEqual(actual_html, expected_html, "Failed to convert a simple ordered list")


test_markdown()
if __name__ == "__main__":
    unittest.main()
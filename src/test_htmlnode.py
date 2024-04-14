import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_rep(self):
        node = HTMLNode("a", "link", [], {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual("HTMLNode(a, link, [], {'href': 'https://www.boot.dev', 'target': '_blank'})", repr(node))
    
    def test_props_to_html(self):
        node = HTMLNode("a", "link", [], {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

if __name__ == "__main__":
    unittest.main()
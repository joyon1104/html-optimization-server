from mcp.server.fastmcp import FastMCP # Parameter is not strictly needed now, but good practice to keep if you add more complex params later
from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
import os

# Create the FastMCP instance with stdio transport
mcp = FastMCP()

# Define the tool using the @mcp.tool() decorator
@mcp.tool()
def get_html_optimization(html_content: str) -> str:
    """
    Optimizes the given HTML content for better performance and SEO.

    :param html_content: The HTML content to be optimized
    :return: The optimized HTML content
    """
    # templates 폴더의 템플릿 파일에서 내용 읽기
    template_path = os.path.join(os.path.dirname(__file__), "templates", "html_opt_template.txt")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    prompt = PromptTemplate.from_template(template)

    anthropic_api_key = os.environ.get('ANTHROPIC_API_KEY')
    chat_model = ChatAnthropic(
        anthropic_api_key=anthropic_api_key,
        model_name="claude-4-sonnet-20250514"
    )
    optimized_html = chat_model.invoke(prompt.format(html_content=html_content))
    
    return optimized_html.content

# The tool is automatically added to the mcp instance by the decorator

# Run the server if the script is executed directly
# if __name__ == "__main__":
#    print("Starting MCP server...")
#    mcp.run(transport="stdio")

if __name__ == "__main__":
    # MCP 서버 대신 직접 함수 호출로 테스트
    test_html = "<div style='color:red;'>테스트</div>"
    result = get_html_optimization(test_html)
    print(result)
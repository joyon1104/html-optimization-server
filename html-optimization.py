from mcp.server.fastmcp import FastMCP # Parameter is not strictly needed now, but good practice to keep if you add more complex params later
from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic

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
    # Placeholder for actual optimization logic
    template = """
    아래는 Figma에서 자동 변환된 복잡하고 인라인 스타일이 많아 유지보수가 어려운 HTML 코드입니다.
    이 코드를 다음 조건을 충족하는 최적화된 형태로 개선해 주세요.

    - 인라인 스타일을 최대한 CSS 클래스와 외부 스타일시트로 분리
    - 불필요한 중첩된 div 태그 제거 및 간결한 구조로 변경
    - 시맨틱한 HTML5 태그(예: header, section, button 등) 활용
    - 코드 가독성과 유지보수성 향상
    - 디자인 토큰(색상, 폰트 등)은 CSS 변수로 정리
    - 기능적인 부분은 유지하며 코드 용량과 복잡도 최소화

    아래는 최적화 대상 코드입니다. 코드를 리팩토링한 후에는 작성한 CSS 코드도 함께 제공 부탁드립니다.

    ```html
    {html_content}
    ```"""
    prompt = PromptTemplate.from_template(template)

    anthropic_api_key = ""
    chat_model = ChatAnthropic(
        anthropic_api_key=anthropic_api_key,
        model_name="claude-4-sonnet-20250514"
    )
    optimized_html = chat_model.invoke(prompt.format(html_content=html_content))
    
    return optimized_html.content

# The tool is automatically added to the mcp instance by the decorator

# Run the server if the script is executed directly
if __name__ == "__main__":
   print("Starting MCP server...")
   mcp.run(transport="stdio")

# if __name__ == "__main__":
#     # MCP 서버 대신 직접 함수 호출로 테스트
#     test_html = "<div style='color:red;'>테스트</div>"
#     result = get_html_optimization(test_html)
#     print(result)
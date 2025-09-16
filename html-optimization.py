from mcp.server.fastmcp import FastMCP # Parameter is not strictly needed now, but good practice to keep if you add more complex params later
from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic

import os
import json
import datetime

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
        model_name="claude-4-sonnet-20250514",
        max_tokens=16000
    )
    optimized_html = chat_model.invoke(prompt.format(html_content=html_content))
    
    return optimized_html.content


def get_html_optimization_test_input() -> str:
    """
    Optimizes the HTML content from a test input file for better performance and SEO.

    :return: The optimized HTML content
    """
    # test_inputs 폴더의 테스트용 HTML 파일에서 내용 읽기
    input_path = os.path.join(os.path.dirname(__file__), "test_inputs", "figma_layout.html")
    with open(input_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # templates 폴더의 템플릿 파일에서 내용 읽기
    template_path = os.path.join(os.path.dirname(__file__), "templates", "html_opt_template.txt")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    prompt = PromptTemplate.from_template(template)

    anthropic_api_key = os.environ.get('ANTHROPIC_API_KEY')
    chat_model = ChatAnthropic(
        anthropic_api_key=anthropic_api_key,
        model_name="claude-4-sonnet-20250514",
        max_tokens=16000
    )
    optimized_html = chat_model.invoke(prompt.format(html_content=html_content))
    
    return optimized_html.content

def get_html_optimization_file(result: str):
    # 결과 저장 기본 디렉터리
    result_dir = os.path.join(os.path.dirname(__file__), "result")
    os.makedirs(result_dir, exist_ok=True)

    # 하위 폴더명 예: 현재 시각 기반 'YYYYMMDD_HHMMSS' 형식
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = os.path.join(result_dir, timestamp)
    os.makedirs(session_dir, exist_ok=True)

    # json 파일 저장
    result_path = os.path.join(session_dir, "optimized_result.json")
    with open(result_path, "w", encoding="utf-8") as f:
        f.write(result)

    # JSON 파일 읽기
    with open(result_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # html 파일로 저장
    html_path = os.path.join(session_dir, "optimized.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(data.get("html", ""))

    # css 파일로 저장
    css_path = os.path.join(session_dir, "optimized.css")
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(data.get("css", ""))

# # Run the server if the script is executed directly
# if __name__ == "__main__":
#    print("Starting MCP server...")
#    mcp.run(transport="stdio")

if __name__ == "__main__":
    # MCP 서버 대신 직접 함수 호출로 테스트
    # test_html = "<div style='color:red;'>테스트</div>"
    # result = get_html_optimization(test_html)
    # print(result)
    
    result = get_html_optimization_test_input()
    get_html_optimization_file(result)
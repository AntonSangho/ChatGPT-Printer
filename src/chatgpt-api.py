import requests
from escpos.printer import Serial

# ChatGPT API를 사용하여 데이터 가져오기
def get_chatgpt_response(prompt):
    # ChatGPT API의 엔드포인트와 인증 토큰을 설정
    url = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",  # 여기에 API 키를 입력하세요.
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150  # 필요한 토큰 수를 조정하세요.
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    return response_json.get('choices')[0].get('text')

# 열전사 프린터로 텍스트 출력
def print_to_thermal_printer(text):
    # 프린터 설정 (포트와 설정에 따라 변경 필요)
    printer = Serial(devfile='/dev/ttyS0', baudrate=19200)

    # 텍스트 출력
    printer.text(text)
    printer.cut()

# 메인 함수
def main():
    # ChatGPT에 전달할 프롬프트
    prompt = "라즈베리파이와 열전사 프린터를 사용한 프로젝트 예시"

    # ChatGPT API로부터 응답 받기
    response_text = get_chatgpt_response(prompt)

    # 응답을 프린터로 출력
    print_to_thermal_printer(response_text)

if __name__ == "__main__":
    main()

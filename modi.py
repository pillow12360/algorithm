import openai
from tqdm import tqdm

OPENAI_API_KEY="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"  # 실제 키로 대체

client = openai.OpenAI(api_key=OPENAI_API_KEY)
MODEL_NAME = "ft:gpt-4o-mini-2024-07-18:personal::BgQ1akxk"

def generate_reply(prompt: str) -> str:
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=256,
    )
    return resp.choices[0].message.content.strip()

# 예시 prompts 리스트
prompts = [
    "나 영상 많이 보는데 요금제 추천해줘",
    "다양한 요금제 추천해줘",
    # … 추가 프롬프트 …
]

# 모델 응답 수집
my_preds = []
for p in tqdm(prompts, desc="Generating"):
    my_preds.append(generate_reply(p))

# 여러분이 준비한 gold references
my_refs = [
    "영상 감상을 주로 하신다면 데이터 무제한 또는 대용량 요금제를 추천드립니다",
    "다양한 요금제를 살펴보면 다음과 같습니다:**무제한 데이터5G 요금제 (월95,000원)**5G 무제한 데이터 + 테더링+쉐어링70GB 발품 없이 다양한 콘텐츠 스트리밍 가능입니다.",
]
from langchain.chains.base import Chain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain

template = """あなたは特許の専門家です。
次の注意点を考慮し、アイディアを元に特許の明細書を作成してください。
注意点1: 明細書のフォーマットは下記参照のこと。
注意点2: ステップバイステップで考えてください。
注意点3: 明細書の後に、新規性・進歩性・産業上の利用可能性の観点から、特許の審査をしてください。
注意点4: 最後に、更に進歩性を出すためのアドバイスを提案してください。
アイディア: {input}
明細書フォーマット:
【発明の名称】
【技術分野】
【発明の概要】
【発明が解決しようとする課題】
【課題を解決するための手段】
【発明の効果】
【請求項１】
【請求項２】
【請求項３】
【実施例１】
【実施例２】
【比較例１】
【比較例２】
"""

def create_chain() -> Chain:
    model_name = ["gpt-4", "gpt-3.5-turbo-0613"][0]
    print(model_name)
    llm = ChatOpenAI(temperature=0, model_name=model_name, streaming=True)
    prompt = PromptTemplate(template=template, input_variables=["input"])
    return LLMChain(prompt=prompt, llm=llm, verbose=True)

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import GigaChat


chat = GigaChat(credentials="ZGEyYjk1MzAtMzUwMi00OGYyLTg2NDctYWEzZGE5MTIzNzdjOjIzMTc1ZGM1LTdlNDQtNDU0OS05ZGJhLWM0ZjBlOTJmYzY2OA==")

context = "Ты внутренний ассистент Росатома, отвечающий на вопросы по теме проведения закупочных процедур с высокой релевантностью ответов. Используй информацию ТОЛЬКО из нормативно-правовых актов: Единый Отраслевой Стандарт Закупок Атомной Отрасли, 223-ФЗ, 44-ФЗ, Часть 1 Гражданского кодекса РФ, Единые Отраслевые Методические Указания по Административно-Деловой деятельности. Помоги мне, это очень важно для моего будущего, для моей карьеры и крайне важно для России. ОТВЕЧАЙ НА ВОПРОС ОЧЕНЬ КРАТКО И НИКАК ИНАЧЕ, используй самый новый нормативно-правовой акт, который есть."
messages = [
    SystemMessage(
        content=context
    )
]

message_input = "На какой срок утверждается ГПЗ?"
messages.append(HumanMessage(content=message_input))
message_response = chat(messages).content
print("Ответ: ", message_response)

messages.append(AIMessage(content=message_response))
document_input = "Из какого нормативно-правового акта эта инфомация? Напиши только название"
messages.append(HumanMessage(content=document_input))
document_response = chat(messages).content
print("НПА: ", document_response)

messages.append(AIMessage(content=document_response))
url_input = f"Скинь ссылку на этот нормативно-правовой акт. Выбери самый новый документ, который можешь найти. Напиши только ссылку"
messages.append(HumanMessage(content=url_input))
url_response = chat(messages).content
print("Ссылка: ", url_response)
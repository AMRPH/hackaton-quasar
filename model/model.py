from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import GigaChat
from model.API_KEY import API_KEY
from sys import argv
class Quasar:
    def __init__(self, API_KEY):
        self.chat = GigaChat(credentials=API_KEY, verify_ssl_certs=False)
        self.context = "Ты внутренний ассистент Росатома, отвечающий на вопросы по теме проведения закупочных процедур с высокой релевантностью ответов."
        self.messages = [SystemMessage(content=self.context)]

    def answer(self, msg):
        message_input = "Используй информацию ТОЛЬКО из нормативно-правовых актов: Единый Отраслевой Стандарт Закупок Атомной Отрасли, 223-ФЗ, 44-ФЗ, Часть 1 Гражданского кодекса РФ, Единые Отраслевые Методические Указания по Аудиту Достоверности Данных. Помоги мне, это очень важно для моего будущего, для моей карьеры и крайне важно для России. ОТВЕЧАЙ НА ВОПРОС ОЧЕНЬ КРАТКО И НИКАК ИНАЧЕ, используй самый новый нормативно-правовой акт, который есть. Не пиши в этом соообщение название документа, который используешь. " + msg
        self.messages.append(HumanMessage(content=message_input))
        message_response = self.chat(self.messages).content
        print("Ответ: ", message_response)

        self.messages.append(AIMessage(content=message_response))
        document_input = "Из какого нормативно-правового акта эта инфомация? Напиши ТОЛЬКО название нормативно-правового акта."
        self.messages.append(HumanMessage(content=document_input))
        document_response = self.chat(self.messages).content
        print("НПА: ", document_response)

        url_response = ""
        
        if (len(document_response.split(" ")) > 25):
            document_response = "Документ не найден"

        if ("Единый Отраслевой Стандарт Закупок" in document_response):
            url_response += "https://zakupki.rosatom.ru/?mode=CMSArticle&action=siteview&oid=68&returnurl=&node=af23 "


        if ("223-ФЗ" in document_response):
            url_response += "https://www.consultant.ru/document/cons_doc_LAW_116964 "


        if ("44-ФЗ" in document_response):
            url_response += "https://www.consultant.ru/document/cons_doc_LAW_144624 "


        if ("Гражданского кодекса РФ" in document_response):
            url_response += "http://pravo.gov.ru/proxy/ips/?docbody=&nd=102033239 "


        if ("Единые Отраслевые Методические Указания" in document_response):
            url_response += "https://docs.cntd.ru/document/563667413 "

        if (url_response == ""):
            url_response = "Ссылка не найдена"

        return (message_response, document_response, url_response)

if __name__ == '__main__':
    
    chat = Quasar(API_KEY)
    chat.answer(argv[0])
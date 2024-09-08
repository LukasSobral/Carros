from openai import OpenAI


client = OpenAI(
    api_key='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'
)


def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content
import flet as ft
import requests


def main(page: ft.Page):
    page.title = "Прогноз погоды"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Укажите город', width=400)
    weather_data = ft.Text('')
    feels = ft.Text('')
    weather_info = ft.Text('')

    def get_info(event):
        if len(user_data.value) < 2:
            return

        API = '7973027923ab37805b180bdeab55e146'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric&lang=ru'
        result = requests.get(URL).json()
        # print(result)
        temperature = result['main']['temp']
        feels_like = result['main']['feels_like']
        weather = result['weather'][0]['description']
        feels.value = 'Чувствуется как: ' + str(round(feels_like, 0)) + ' °C'
        weather_data.value = 'Температура: ' + str(round(temperature, 0)) + ' °C'
        weather_info.value = 'Погода: ' + str(weather)
        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text('Прогноз погоды')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                user_data
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                weather_data
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                feels
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                weather_info
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.ElevatedButton(text='Получить', on_click=get_info)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )


ft.app(target=main)

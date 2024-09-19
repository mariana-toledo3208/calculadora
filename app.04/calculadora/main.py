import flet as ft 


def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        Num1=float(txtNum1.value.string())
        Num2=float(txtNum1.value.string())
        resultado=Num1+Num2
        lblResultado.value="Resultado: {Resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
        
        
    page.title = "calculadora"
    page.bgcolor="green"
    
    txtNum1=ft.TextField(label="Ingresa el primer numero",color="yellow")
    txtNum2=ft.TextField(label="Ingresa el segundon numero",color="yellow")
    lblResultado=ft.Text("Resultado: ",color="yellow")
    btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnResta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnMultiplicacion=ft.ElevatedButton(text="*",on_click=on_calc_multiplicacion)
    btnDivision=ft.ElevatedButton(text="/",on_click=on_calc_division)
    
    
page.add(
    ft.Colum(controls=[
        ft.Row(controls=[
            txtNum1,
            txtNum2
        ],alignment="center")
        ]),
        ft.Row(controls=[lblResultado],alignment="center"),
        ft.Row(controls=[
            btnSuma,
            btnResta,
            btnMultiplicacion,
            btnDivision
            ],alignment="center")
        ]
    )
)


ft.app(main)

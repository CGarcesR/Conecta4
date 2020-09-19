from conecta4_mejorado import *

ventana.title("Conecta 4")

boton1 = tk.Button(ventana, text="1", command = lambda: colocarFichas(0))
boton2 = tk.Button(ventana, text="2", command = lambda: colocarFichas(1))
boton3 = tk.Button(ventana, text="3", command = lambda: colocarFichas(2))
boton4 = tk.Button(ventana, text="4", command = lambda: colocarFichas(3))
boton5 = tk.Button(ventana, text="5", command = lambda: colocarFichas(4))
boton6 = tk.Button(ventana, text="6", command = lambda: colocarFichas(5))
boton7 = tk.Button(ventana, text="7", command = lambda: colocarFichas(6))

boton1.grid(row=0 ,column=1,padx=4,pady=5)
boton2.grid(row=0 ,column=2,padx=4,pady=5)
boton3.grid(row=0 ,column=3,padx=4,pady=5)
boton4.grid(row=0 ,column=4,padx=4,pady=5)
boton5.grid(row=0 ,column=5,padx=4,pady=5)
boton6.grid(row=0 ,column=6,padx=4,pady=5)
boton7.grid(row=0 ,column=7,padx=4,pady=5)

actualizar()
ventana.mainloop()

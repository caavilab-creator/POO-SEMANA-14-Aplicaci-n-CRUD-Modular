import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante


class AppVisitas(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        # Variable de estado para rastrear qué visitante está seleccionado
        self._cedula_seleccionada = None
        
        self.title("Gestión de Visitantes - Sistema CRUD")
        self.geometry("750x450")
        self.configure(bg="#f4f4f9")
        
        self._aplicar_estilos()
        self._configurar_interfaz()
        self._actualizar_tabla()  # Cargar datos iniciales si los hay
    
    def _aplicar_estilos(self):
        style = ttk.Style(self)
        style.theme_use('clam')  # Tema visual más limpio
        
        # Estilo de la tabla
        style.configure("Treeview", background="#ffffff", foreground="#333333", rowheight=25)
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#e0e0e0")
        style.map('Treeview', background=[('selected', '#4a90e2')])  # Azul al seleccionar fila
        
        # Estilos semánticos para botones (UX)
        style.configure("Guardar.TButton", font=("Arial", 10, "bold"), background="#4CAF50", foreground="white", padding=5)
        style.configure("Actualizar.TButton", font=("Arial", 10, "bold"), background="#2196F3", foreground="white", padding=5)
        style.configure("Eliminar.TButton", font=("Arial", 10, "bold"), background="#f44336", foreground="white", padding=5)
        style.configure("Limpiar.TButton", font=("Arial", 10, "bold"), background="#9e9e9e", foreground="white", padding=5)
    
    def _configurar_interfaz(self):
        # --- Frame del Formulario ---
        frame_form = tk.Frame(self, bg="#f4f4f9")
        frame_form.pack(pady=15, padx=20, fill="x")
        
        tk.Label(frame_form, text="Cédula:", bg="#f4f4f9", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_cedula = ttk.Entry(frame_form, width=20)
        self.ent_cedula.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_form, text="Nombre:", bg="#f4f4f9", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.ent_nombre = ttk.Entry(frame_form, width=35)
        self.ent_nombre.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(frame_form, text="Motivo:", bg="#f4f4f9", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ent_motivo = ttk.Entry(frame_form, width=64)
        self.ent_motivo.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")
        
        # --- Frame de Botones ---
        frame_btns = tk.Frame(self, bg="#f4f4f9")
        frame_btns.pack(pady=5, padx=20, fill="x")
        
        ttk.Button(frame_btns, text="Agregar", style="Guardar.TButton", command=self._registrar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Actualizar", style="Actualizar.TButton", command=self._actualizar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Eliminar", style="Eliminar.TButton", command=self._eliminar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Limpiar", style="Limpiar.TButton", command=self._limpiar_campos).pack(side=tk.RIGHT, padx=5)
        
        # --- Tabla (Treeview) ---
        frame_tabla = tk.Frame(self)
        frame_tabla.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.tabla = ttk.Treeview(frame_tabla, columns=("Cédula", "Nombre", "Motivo"), show='headings')
        self.tabla.heading("Cédula", text="Cédula")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Motivo", text="Motivo")
        
        # Evento: Al hacer clic en una fila, cargar datos en el formulario
        self.tabla.bind("<<TreeviewSelect>>", self._seleccionar_fila)
        self.tabla.pack(fill="both", expand=True)
    
    # --- Lógica de Eventos de la UI ---
    def _seleccionar_fila(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            item = self.tabla.item(seleccion[0])
            valores = item['values']
            self._limpiar_campos()
            
            # Guardamos la cédula en la memoria de la clase (Estado)
            self._cedula_seleccionada = str(valores[0])
            
            # Llenar campos
            self.ent_cedula.insert(0, valores[0])
            self.ent_nombre.insert(0, valores[1])
            self.ent_motivo.insert(0, valores[2])
            
            # Bloqueamos la UI para que no modifiquen la llave primaria
            self.ent_cedula.config(state="disabled")
    
    def _registrar(self):
        # Leemos los datos de la UI
        cedula = self.ent_cedula.get().strip()
        nombre = self.ent_nombre.get().strip()
        motivo = self.ent_motivo.get().strip()
        
        try:
            # La creación del objeto VA DENTRO del try, porque el modelo puede lanzar error
            nuevo = Visitante(cedula, nombre, motivo)
            self.servicio.registrar_visitante(nuevo)
            self._actualizar_tabla()
            self._limpiar_campos()
            messagebox.showinfo("Éxito", "Visitante registrado correctamente.")
        except ValueError as e:
            messagebox.showwarning("Atención", str(e))
    
    def _actualizar(self):
        if not self._cedula_seleccionada:
            messagebox.showwarning("Atención", "Seleccione un visitante de la tabla para actualizar.")
            return
        
        nombre = self.ent_nombre.get().strip()
        motivo = self.ent_motivo.get().strip()
        
        try:
            # Usamos la cédula guardada en memoria, no dependemos de leer el widget deshabilitado
            visitante_editado = Visitante(self._cedula_seleccionada, nombre, motivo)
            self.servicio.actualizar_visitante(visitante_editado)
            self._actualizar_tabla()
            self._limpiar_campos()
            messagebox.showinfo("Éxito", "Registro actualizado.")
        except ValueError as e:
            messagebox.showwarning("Atención", str(e))
    
    def _eliminar(self):
        if not self._cedula_seleccionada:
            messagebox.showwarning("Atención", "Seleccione un visitante de la tabla para eliminar.")
            return
        
        respuesta = messagebox.askyesno("Confirmar", f"¿Seguro que desea eliminar la cédula {self._cedula_seleccionada}?")
        if respuesta:
            try:
                self.servicio.eliminar_visitante(self._cedula_seleccionada)
                self._actualizar_tabla()
                self._limpiar_campos()
                messagebox.showinfo("Éxito", "Visitante eliminado.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
    
    def _actualizar_tabla(self):
        # Limpiar tabla actual
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Cargar datos desde el servicio
        for v in self.servicio.obtener_todos():
            self.tabla.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))
    
    def _limpiar_campos(self):
        self._cedula_seleccionada = None  # Reseteamos el estado
        self.ent_cedula.config(state="normal")
        self.ent_cedula.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_motivo.delete(0, tk.END)
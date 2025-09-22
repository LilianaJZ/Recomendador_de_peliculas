class Usuario_Premium:

    def __init__(self, id,  nombre, correo, contrasena, flag_premium ,tipo_plan,  fecha_inicio, fecha_final):
        super().__init__(self, id,  nombre, correo, contrasena)
        self.flag_premium = flag_premium
        self.tipo_plan = tipo_plan
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final


    # Getter and Setter
    @property
    def flag_premium(self):
        return self._flag_premium

    @flag_premium.setter
    def flag_premium(self, flag_premium):
        self._flag_premium = flag_premium

    # --- Propiedad para 'tipo_plan' ---
    @property
    def tipo_plan(self):
        return self._tipo_plan

    @tipo_plan.setter
    def tipo_plan(self, tipo_plan):
        self._tipo_plan = tipo_plan

    # --- Propiedad para 'fecha_inicio' ---
    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    # --- Propiedad para 'fecha_final' ---
    @property
    def fecha_final(self):
        return self._fecha_final

    @fecha_final.setter
    def fecha_final(self, fecha_final):
        self._fecha_final = fecha_final
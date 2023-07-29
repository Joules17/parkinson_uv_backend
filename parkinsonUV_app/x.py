# Supongamos que ya tienes algunos pacientes y terapeutas creados
# Si no tienes datos en estas tablas, asegúrate de crearlos primero

# Obtener pacientes y terapeutas (puedes usar get() o filter() dependiendo de tu caso)
patient1 = Patient.objects.get(user_id_id="google-oauth2|112748547430075285233")
patient2 = Patient.objects.get(user_id_id="google-oauth2|111734557734355383314")
therapist = Therapist.objects.get(user_id_id="google-oauth2|114369132100672370742")

# Crear una nueva lista y guardarla en la base de datos
new_list = List(name="Lista de Ejemplo 1")
new_list.save()

# Agregar relaciones muchos a muchos con pacientes y terapeutas
new_list.patients.add(patient1, patient2)
new_list.therapists.add(therapist)

from parkinsonUV_app.models import Patient, Therapist, List
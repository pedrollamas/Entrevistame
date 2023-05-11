#--------------------LIBRERÍAS--------------------#
import streamlit as st
from streamlit_extras.badges import badge

import base64
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#--------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
st.set_page_config(page_title="Pedro Llamas", layout="wide", page_icon="ℹ️")
st.set_option('deprecation.showPyplotGlobalUse', False)

hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)



st.write("""
<style>
h1, h2, h3, h4, h5, h6 {
    font-family: 'Verdana';
}
</style>
""", unsafe_allow_html=True)

container = st.container()
with container:
    
    st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
            <div style='font-size: 35px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>¡Bienvenida/o!</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Con el objetivo de faciliar el trabajo de los entrevistadores, he creado esta app de streamlit con una serie de información que puede ser de utilidad para conocerme mejor como candidato.</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Si viene redirigida/o desde mi CV no lo necesita, pero aquí debajo encontrará mi CV por si no lo tiene y desea descargarlo.</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Haga click en el botón 'Descargar CV en PDF' justo debajo de la imagen.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col3:
        st.markdown("""  """)
        st.image("img/cv.png", width=150)
        # Lee el archivo PDF en formato binario
        with open('data/PEDRO LLAMAS LÓPEZ CV.pdf', 'rb') as f:
            pdf_data = f.read()

        # Codifica el archivo PDF en base64
        b64_pdf = base64.b64encode(pdf_data).decode('utf-8')

        # Genera el enlace de descarga para el archivo PDF
        href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="cv.pdf">Descargar mi CV en PDF</a>'

        # Muestra el enlace de descarga en Streamlit
        st.markdown(href, unsafe_allow_html=True)

    st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Ahora pasamos a la sección de preguntas y respuestas.</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'></div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'></div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Debajo encontrarás 11 categorías de preguntas a las que puedes acceder con sus respectivas respuestas.</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(""" """)
    col1, col2, col3 = st.columns(3)
    with col2:
        categoria = st.selectbox("Selecciona una categoría de preguntas", 
                                            ["Sobre mi", 
                                            "Experiencia y habilidades",
                                            "Trabajo en equipo y habilidades interpersonales",
                                            "Resolución de problemas y toma de decisiones",
                                            "Metas y motivación",
                                            "Adaptabilidad y flexibilidad",
                                            "Capacidad de resiliencia",
                                            "Expectativas salariales y disponibilidad",
                                            "Aprendizaje y desarrollo profesional",
                                            "Habilidades de comunicación",
                                            "Motivación y compromiso con la empresa"                                        
                                            ])
    if categoria == "Sobre mi":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 30px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Preguntas sobre mi.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cuáles son tus principales fortalezas y debilidades?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Yo diría que mis principales fortalezas son la alta capcidad de aprendizaje, la empatía y la ambición. La primera creo que viene dada porque tengo una mente curiosa, cualquier tema me genera interés y me educaron a escuchar antes que hablar por lo que acudo a formarme y escuchar a gente con más experiencia. La empatía creo que me permite trabajar en equipo con mucha mayor seguridad y entendiendo las necesidades de clientes y compañeros como mías. Y por último, creo que la ambición me proporciona el hambre suficiente para mantener activa esa necesidad continua de aprender.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo te describirían tus anteriores compañeros de trabajo?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>No me gusta hablar por nadie, pero creo que destacarían la relación personal lo primero, que es muy importante para mi en un ambiente de trabajo y estoy seguro que esas ganas de aprender junto con mi insistencia por adquirir los conocimientos que se esperan de mi y generar nuevas ideas continuamente.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cuáles son los factores más determinantes para ti a la hora de elegir una empresa?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Para mí, los factores más determinantes a la hora de elegir una empresa son aquellos que fomenten mi crecimiento profesional y me permitan mantenerme a la vanguardia de la ciencia de datos. Valoraría una cultura de aprendizaje continuo, la disponibilidad de recursos y capacitaciones en tecnologías y metodologías avanzadas, así como la oportunidad de trabajar en proyectos desafiantes e innovadores. Además, buscaría un entorno colaborativo, donde pueda interactuar con profesionales talentosos y compartir conocimientos para impulsar mi desarrollo en el campo de la ciencia de datos.</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'></div>
        </div>
        """,
        unsafe_allow_html=True)
    
    elif categoria == "Experiencia y habilidades":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Experiencia y habilidades.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Por qué decidiste orientarte hacia la ciencia y análisis de datos?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Siempre en mis experiencias personales y sobre todo profesionales he buscado soluciones a problemas de la manera más objetiva posible y eso me ha encaminado siempre a los datos que es la fuente de objetividad más pura que tenemos de cara a tomar decisiones. Me faltaban los conocimentos técnicos de herramientas para poder darle un mejor uso y por ello acudí a formarme en este ámbito.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Has vivido experiencias internacionales?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Si, desde pequeño siempre he realizado numerosos viajes, habiendo estado en más de 30 países, he residido en Irlanda 2 meses de adolescente, 1 año en Kansas,EEUU donde perfeccioné mi inglés y 1 año en París durante mi experiencia Erasmus. Siempre estoy abierto a conocer nuevos horizontes y por eso disfruto mucho de los ambientes laborales multiculturales.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cuáles son tus habilidades más relevantes?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Primero yo creo que sería mi tenacidad por adquirir habilidades, soy de las personas que considera que nada es imposible de aprender si se dedica el tiempo suficiente. Algo que he aprendido también por mi educación y experiencia es a disfrutar del trabajo bien hecho, tengo una alta consciencia de equipo y creo que el éxito a nivel grupal se consigue a través de los objetivos. Por último, me gusta considerarme una persona que tiene una visión global de los negocios y me suele ser sencillo identificar prioridades en el trabajo y eso creo que es muy valorable de cara al ámbito laboral.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo te mantienes actualizado/a en tu campo de trabajo?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Actualmente intento fortalecer aquellas habilidades que considero que tengo margen de mejora, que siempre son todas. Pero sobre todo, pregunto a gente a través de portales o profesores míos cuáles consideran que son las herramientas que van a tener un mayor impacto en el sector. Desde ese conocimiento me marco una hoja de ruta con lo que tengo que aprender para mejorar en este ámbito.</div>
        </div>
        """,
        unsafe_allow_html=True)
    
    elif categoria == "Trabajo en equipo y habilidades interpersonales":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Trabajo en equipo y habilidades interpersonales.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>Cuéntame sobre una situación en la que trabajaste en equipo para lograr un objetivo.</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Creo que no existe una situación laboral en la que una única persona logre un objetivo por el resto, siempre en mayor o menor medida necesitas estar en sinergia con tus compañeros. En todos los trabajos que he tenido, he necesitado de la colaboración de compañeros para la consecución de objetivos. Desde estar en contacto continúo con otros departamentos en los procesos de selección que he trabajado, hasta la coordinación de los puntos de mejora con clientes. Creo que aprendí a trabajar en equipo de manera efectiva en Dekuplé ya que en cada proyecto estaban involucrados todos los departamentos y supe adaptar mi manera de trabajar a cada departamento, estableciendo prioridades para facilitar su trabajo.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo manejas los conflictos en el trabajo?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>De la forma más natural posible, pidiendo al compñaero o compañera un momento privado para exponerle aquello que considero que se puede hacer mejor y escuchando su réplica para llegar a un punto en común. Cuando pones en común</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo te comunicas efectivamente con personas de diferentes niveles y departamentos?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Intento siempre acudir a mi senior o jefe directo, en función de la urgencia del asunto o bien a través de las reuniones periódicas o sprints o si se trata de un asunto urgente pidiendole un hueco en su agenda para ello. He trabajado siempre con herramientas ágiles que te permiten ver la disponibilidad de los compañeros y compañeras, lo cual facilita mucho el trabajo y es más dinámico.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo te adaptas a trabajar en un equipo diverso?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Cuando entro a una nueva empresa intento siempre preguntar cómo funcionan los procesos en la empresa, las prácticas habituales e intento seguirlas todo lo que puedo. No he tenido una experiencia en la que me haya costado adaptarme por suerte. Me siento muy cómodo en ambientes diversos ya que aprendes continuamente y se trata siempre de aportar a esa diversidad y enriquecerse unos de otros.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo lideras y motivas a otros?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Siempre me gusta considerar que a través del ejemplo, ser yo y mantener esa cordialidad y profesionalidad de la que estoy orgulloso. Considero que tengo de manera innata la capacidad de ver las habilidades de otras personas y si alguien me solicita consejo sobre una cuestión, me gusta hacer ver a la persona que tiene las habilidades para llevarlo a cabo. A veces las personas necesitamos simplemente una muestra de confianza para cumplir objetivos y metas profesionales o personales. Aún no he tenido experiencia laboral en puestos de gestión pero aspiro a tenerlo en el futuro.</div>
        </div>
        """,
        unsafe_allow_html=True)
            
    elif categoria == "Resolución de problemas y toma de decisiones":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Resolución de problemas y toma de decisiones.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>Cuéntame sobre un desafío difícil que enfrentaste en el trabajo y cómo lo superaste.</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Cuando trabajaba de Project Manager nos enfrentabamos continuamente a situaciones difíciles relacionadas con los deadlines. A veces los clientes solicitaban servicios para fechas determinadas y ahí entra el trato humano para por un lado tener a todos los equipos con el foco puesto en una fecha y por otro lado tener al cliente al corriente de los avances. Cuando por razones inesperadas no se puede cumplir una deadline, es importante demostrar a los clientes que el equipo ha puesto el 100% en la tarea y cuando es comprensivo hacerle ver lo agradecido que estás y compensarle con más trabajo.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo abordas los problemas de manera sistemática?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Yo uso una metodología para los problemas y tareas diarias, semanales, mensuales, etc. Siempre suelo anotar al principio de cada semana y cada día las tareas por un lado obligatorias, es decir, aquellas que tienen que estar realizadas en el día. En otro lado anoto las que tienen que ser realizadas en la semana y por último anoto tareas o ideas que son a futuro. Con esas tres categorías se genera un círculo, cuando las tareas diarias se cumplen, entran las semanales y las de futuro pasan a tener ya un deadline semanal. De esta forma establezco unas prioridades y se van cumpliendo todas.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo tomas decisiones cuando no tienes toda la información necesaria?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Pregunto a las personas que tienen los conocimientos necesarios y con ello adquiero yo conocimiento para ir formulando mi decisión. Si es un tema del que no tengo ningún tipo de conocimiento me informo previamente con diferentes herramientas y pregunto a posteriori. Siempre hay que tener en cuenta la perspectiva de las personas que viven los procesos, problemas o tareas de cerca porque te dan una información real del problema y luego desde tu perspectiva más ajena, normalizas ese problema para buscar la forma más efectiva de solucionarlo.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo manejas situaciones de alta presión o estrés?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Por lo general soy una persona que disfruta de la sensación de tener cosas que realizar, entonces esa presión que viene dada por tareas a realizar la disfruto. Me cuesta más estar sin tareas que realizar. Si la situación de estrés llega a un punto que se escapa de mi control, acudo a mis compañeros y jefes directos a comentarlo. Desde mi perspectiva no es malo comentar cuando no puedes con una situación, porque casi siempre recibes a cambio consejo por parte de la gente más experimentada que te desbloquea y acabas realizando la tarea que necesitas.</div>
        </div>
        """,
        unsafe_allow_html=True)
    
    elif categoria == "Metas y motivación":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Metas y motivación.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cuál es tu objetivo profesional a largo plazo?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Mi objetivo profesional a largo plazo es adquirir los suficientes conocimientos técnicos para embarcarme en proyectos relacionados con la creación de modelos de Inteligencia Artificial y a largo plazo poder liderar esos proyectos.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Qué te motiva en tu trabajo?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Mi principal fuente de moivación en el trabajo es siempre ese hambre de seguir aprendiendo, me siento muy cómodo en empresas que no se conforman y buscans siempre nuevas vías para fomentar ese aprendizaje en los empleados. Intento siempre anotar y escuchar a los compañeros y compañeras que más tiempo llevan en la empresa para poder luego por mi cuenta adquirir esos conocimientos. Me gusta mucho marcarme referentes en diferentes áreas dentro de la empresa para poder aprender.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo defines el éxito en tu carrera?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Yo creo que el éxito profesional viene dado por la mentalidad de mantenerte hambriento por conseguir nuevas metas y disfrutar del camino siendo consciente del avance que realizas. Personalmente me gusta de vez en cuando parar un momento y analizar el avance que he realizado, atribuirle valor a lo que ya has aprendido me facilita enormemente aprender nuevas cosas.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo te mantienes motivado/a cuando te enfrentas a desafíos?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Un desafío profesional o personal siempre es una manera de adquirir una habilidad que antes no tenías, por eso supone un desafío porque no sabes si tienes las habilidades suficientes para lograrlo. Disfruto mucho de esa sensación de adrenalina sobre lo desconocido y creo que es lo que me mantiene motivado de cara a los desafíos y sobre todo en constante búsqueda de esos desafíos.</div>
        </div>
        """,
        unsafe_allow_html=True)

    elif categoria == "Adaptabilidad y flexibilidad":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Adaptabilidad y flexibilidad.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'> ¿Cómo te adaptas a los cambios en el entorno laboral?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Intento que sea siempre de la manera más natural posible. Ante la incertidumbre de si un cambio puede ser positivo o negativo, la única posibilidad es comprobarlo realmente. Si das lo mejor de ti, al menos tendrás la consciencia tranquila de que lo has intentado de verdad. Normalmente esos cambios en el entorno laboral cuando son intencionados, vienen de una voluntad de mejorar el entorno por parte de gente experimentada. Por lo tanto, intento escuchar los consejos de quienes aplican esos cambios para ayudar a esa mejora y compartiendo mi experiencia respecto a los mismos.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo manejas múltiples tareas y prioridades?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Como he comentado en el apartado anterior, siempre desde la priorización de tareas. Categorizar las tareas te facilita darles prioridad y generas un flow de trabajo que te lleva a ser más eficiente. Por otro lado, siempre pregunto cuando las tareas vienen atribuidas por otras personas el grado de urgencia que tienen para poder acordarlo y cumplir con la meta en el tiempo solicitado.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo te sientes trabajando en un entorno de ritmo rápido?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Me gusta, siempre y cuando esa rápidez venga dada por la capacidad de todos y todas de realizar tareas en el menor tiempo posible. No considero que la rapidez sea una ventaja si no se realiza el trabajo adecuadamente. Si esa rapidez va relacionada con cumplir los sprints y deadlines, es como más cómodo me siento.</div>
        </div>
        """,
        unsafe_allow_html=True)
        
    elif categoria == "Capacidad de resiliencia":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Capacidad de resiliencia.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'> ¿Cómo te recuperas de un fracaso o error?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Los fracasos o errores tienen una connotación negativa por lo general con la que no estoy de acuerdo totalmente, es decir, cuando las cosas salen mal hay que ser conscientes de que no se ha conseguido el objetivo pero por otro lado te da pie a visualizar con el consejo siempre de compañeros y jefes, aquellas cosas que viéndolo con perspectiva harías diferente y en próximas situaciones similares cambiarlas de tu metología.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Qué haces para mantener un equilibrio entre el trabajo y la vida personal?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Para mi es relativamente sencillo, tengo la misma energía para trabajar que para la vida personal entonces intento buscar nuevas vías o retos constantemente, ya sea a través de actividades deportivas que te obligan a estar un día y hora determinada en un sitio o a través de relaciones sociales que te mantienen despierto siempre encuentro momentos para dejar de lado el trabajo. Creo que tener un balance entre ambas facilita enormemente lo efectivo que seas trabajando después.</div>
        </div>
        """,
        unsafe_allow_html=True)
        
    elif categoria == "Expectativas salariales y disponibilidad":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Expectativas salariales y disponibilidad.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>  ¿Cuáles son tus expectativas salariales?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Me encuentro actualmente cuando escribo esto entre los 24.000 - 28.000. Todo depende siempre de muchas variantes alrededor del salario, hay otras variables como formarciones, planes y demás que pueden modificar esta expectativa salarial. Te recomiendo que si es para un puesto concreto me mandes un email a pedrollamaslopez@hotmail.com y me consultes al respecto.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Estás dispuesto/a a viajar o trabajar horas extras según sea necesario?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Bueno yo lo veo como una ventaja un trabajo que me facilite viajar entonces por esa parte no tengo ningún problema, todo lo contrario. Respecto a las horas extras, creo que es parte de cualquier trabajo y en momentos de urgencia o necesidad dedicarle más horas de lo pactado. Al fin y al cabo creo que mientras la empresa y el empleado se mantengan en la misma página y se entiendan con las condiciones hay que hacer terminar el trabajo que es el fin último siempre.</div>
        </div>
        """,
        unsafe_allow_html=True)        

    elif categoria == "Aprendizaje y desarrollo profesional":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Aprendizaje y desarrollo profesional.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'> Cuéntame sobre una ocasión en la que tuviste que aprender rápidamente una nueva habilidad o concepto.</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Siempre en los trabajos que he tenido me he visto en situaciones donde tenía que aprender nuevas habilidades, desde mis trabajos de estudiante donde tenía que aprender a realizar tareas rápidamente sin dar sensación de urgencia al cliente hasta en mis últimas experiencias laborales donde por ejemplo tenía que manejar datos personales de los clientes de las plataformas o llevar procesos de selección con más de 500 solicitantes. En todas las experiencias laborales se van a dar situaciones nuevas y es parte de lo ilusionante de entrar en una empresa por primera vez.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Qué tipo de entrenamiento o desarrollo profesional te gustaría recibir en tu futura empresa?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Me gustaría que me facilitasen formarme en herramientas que en la empresa o se utilicen actualmente aunque no sea en mi puesto o bien herramientas que tienen pensado implementar a futuro, por ejemplo, me gustaría aprender herramientas cloud como Azure o AWS que estoy cursando actualmente pero perfeccionar mi conocimiento. Quiero por otro lado orientar mi carrera hacia la ciencia de datos y todo lo que sea mejorar mis habilidades con modelos de aprendizaje automático sería bienvenido también.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo buscas oportunidades de crecimiento y aprendizaje en tu carrera?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Cuando me encuentro activamente buscando trabajo, navego principalmente por Linkedin mirando ofertas en empresas que tengan hambre por abrir nuevas puertas en el ámbito de la ciencia de datos o empresas ya consolidadas que puedan proporcionarme ese conocimiento que deseo. Si no me encuentro en búsqueda activa de empleo, me gusta ver que hacen empresas del sector para mantenernos a la vanguardia y poder sugerir cambios. Me gusta en todos los aspectos de mi vida mantenerme lo más informado posible.</div>
        </div>
        """,
        unsafe_allow_html=True)        

    elif categoria == "Habilidades de comunicación":
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Habilidades de comunicación.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo te comunicas efectivamente con diferentes tipos de audiencias (por ejemplo, compañeros de trabajo, clientes, gerentes)?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'> Con compañeros de trabajo, fomento un ambiente colaborativo y utilizo un lenguaje técnico adecuado para transmitir ideas y conceptos de manera clara. Con clientes, adopto un enfoque más orientado a sus necesidades, utilizando un lenguaje accesible y enfocándome en los beneficios y soluciones que puedo ofrecerles. Con los gerentes, presento información de manera concisa y estratégica, destacando los resultados y el impacto de mis acciones en el logro de los objetivos organizacionales. En resumen, adapto mi comunicación para establecer una conexión efectiva con cada tipo de audiencia.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo manejas las presentaciones o discursos en público?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Con todas las presentaciones o discursos públicos como todo en general, dependen de lo trabajados o trabajadas que estén. Intento siempre identificar primero la audiencia que voy a tener para establecer la hoja de ruta primero, hay presentaciones que tienen que ser concisas y orientadas a los resultados y otras que son más formativas que dan pie a empatizar más con la audiencia y tratarlas más como una conversación.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo te aseguras de entender claramente las expectativas y requerimientos de un proyecto o tarea?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Podría resumirlo en 5 pasos que tengo que seguir digamos, empezando por escuchar tanto los requisitos del proyecto como los consejos y necesidades. Realizo preguntas específicas para obtener más detalles sobre los objetivos, plazos, recursos disponibles y cualquier otro aspecto relevante. Esto me ayuda a obtener una visión completa de lo que se espera. Tengo la buena práctica de tomar notas continuamente y posteriormente revisarlas, a veces, lo primero que percibes y anotas te facilita el trabajo después. Por último, documento todo de una manera más clara y organizada para tener definidas las pequeñas tareas que llevan a finalizar el proyecto de la manera adecuada.</div>
        </div>
        """,
        unsafe_allow_html=True)   
        
    elif categoria == "Motivación y compromiso con la empresa" :
        st.markdown(
        """
        <div style='background-color: #85C1E9; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); margin-top: 20px; margin-left: auto; margin-right: auto; width: 60%;'>
        <div style='font-size: 25px; font-weight: 700; margin-bottom: 20px; color: #ffffff;'>Motivación y compromiso con la empresa.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo te mantienes comprometido/a y motivado/a en tu trabajo a largo plazo?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Buscando nuevos retos de manera continua, ya sea por mi cuenta buscar nuevas formas de mejorar los procesos o solicitando consejo para mejorar como profesional. Para mi la motivación y el compromiso van de la mano, aquello que te motiva te genera compromiso de manera implícita.</div>
            <div style='font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #7D3C98;'>¿Cómo contribuirías a la cultura y valores organizacionales de una empresa?</div>
            <div style='font-size: 20px; margin-bottom: 20px; color: #ffffff;'>Algo que siempre siento orgullo en comentar cuando se me pregunta es mis valores, creo que he recibido una educación que se centra en la empatía, en mantenerse abierto constantemente al aprendizaje y en el esfuerzo. Creo que estas tres cosas solo aportan cosas positivas, ya sea a la empresa con la que trabaje o relaciones personales.</div>
        </div>
        """,
        unsafe_allow_html=True)   
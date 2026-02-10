import re

def leer_grupos_preguntas(ruta_fichero):
    with open(ruta_fichero, "r", encoding="utf-8") as f:
        contenido = f.read()
    # Separar por grupos
    grupos_raw = contenido.split('---')
    grupos = list()
    for grupo in grupos_raw:
        # Limpiar espacios en blanco
        grupo = grupo.strip()
        if not grupo:
            continue
        # Separar preguntas
        preguntas = [
            p.strip()
            for p in grupo.split('#')
            if p.strip()
        ]
        grupos.append(preguntas)
    return grupos


def limpiar(pregunta):
    texto = re.sub(r"\b[a-d]\)", "", pregunta)
    texto = re.sub(r"\d+\.", "", texto)
    return texto.strip()


def jaccard(texto1, texto2):
    set1 = set(texto1.lower().split())
    set2 = set(texto2.lower().split())
    return len(set1 & set2) / len(set1 | set2)


def calcula_jaccard(grupo_preguntas):
    resultados = list()
    for grupo in grupo_preguntas:
        grupo_limpio = [limpiar(pregunta) for pregunta in grupo]
        for i_1 in range(0, len(grupo)):
            for i_2 in range(i_1+1, len(grupo)):
                resultados.append(jaccard(grupo_limpio[i_1], grupo_limpio[i_2]))

    return resultados


# Main ------

if __name__ == '__main__':
    grupos_preguntas = leer_grupos_preguntas("./preguntas.txt")
    resultados = calcula_jaccard(grupos_preguntas)
    print("Núemro de reusltados: ", len(resultados))
    str_resultados = [str(num) for num in resultados]
    print("\n".join(str_resultados))



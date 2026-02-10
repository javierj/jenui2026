from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


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


def comparar_preguntas(lista_preguntas):
    emb = model.encode(lista_preguntas)
    return cosine_similarity(emb)


# Main ------
if __name__ == '__main__':
    grupos_preguntas = leer_grupos_preguntas("./preguntas.txt")
    #print(preguntas)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    index = 0
    resultados = list()

    for grupo in grupos_preguntas:
        matrix = comparar_preguntas(grupo)
        print(f"Bloque {index} de {len(grupos_preguntas)} / Preguntas {len(grupo)}")

        print(len(matrix), "\n", matrix)
        for m_i in range(0, len(matrix)-1):
            resultados += list(matrix[m_i][(m_i+1):])
        index += 1

    print("Todos los datos:", len(resultados))
    str_resultados = [str(num) for num in resultados]
    print("\n".join(str_resultados))


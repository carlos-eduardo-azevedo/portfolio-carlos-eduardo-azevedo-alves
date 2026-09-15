
import matplotlib.pyplot as plt



emoji_data = {

  "nome": "Smile",

  "grade": [

    [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)], # Linha 0

    [(255,255,0), (0,0,0),  (255,255,0), (0,0,0),  (255,255,0)], # Linha 1 (Olhos)

    [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)], # Linha 2

    [(255,255,0), (0,0,0),  (0,0,0),  (0,0,0),  (255,255,0)], # Linha 3 (Boca)

    [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)] # Linha 4

  ]

}



plt.imshow(emoji_data["grade"])

plt.show()













biblioteca_musical = {

  "Toques": [

    {"Alegre": ([440, 480], [520, 560])},

    {"Triste": ([200, 150], [100, 50])}

  ]

}





for chave, lista_toques in biblioteca_musical.items():





  for musica in lista_toques:



    for nome, matriz in musica.items():

      print(f"Música: {nome}")

      print("Antes:", list(matriz))





      transposta = [

        [matriz[0][0], matriz[1][0]],

        [matriz[0][1], matriz[1][1]]

      ]



      for linha in transposta:

        print(" linha transposta:", linha)





      musica.update({nome: transposta})



      print("Depois:", musica[nome])







playlist = {

  "nome": "Minha Playlist",

  "imagens": [

    {

      "titulo": "Sol",

      "pixels": (

        (255, 200, 0),

        (255, 220, 50),

        (200, 150, 0)

      )

    },

    {

      "titulo": "Céu",

      "pixels": (

        (100, 150, 255),

        (50, 100, 200),

        (30, 80, 180)

      )

    },

    {

      "titulo": "Grama",

      "pixels": (

        (0, 180, 50),

        (0, 140, 30),

        (50, 200, 80)

      )

    }

  ]

}





nova_imagem = {"titulo": "Fogo", "pixels": ((255,80,0), (255,40,0), (200,20,0))}

playlist["imagens"].insert(0, nova_imagem)





removida = playlist["imagens"].pop()

print(f"Imagem removida: {removida['titulo']}")





for chave in playlist.keys():



  if chave == "imagens":

    for imagem in playlist[chave]:

      print(f" Imagem: {imagem['titulo']}")



      for pixel in imagem["pixels"]:

        print(f"  pixel: {pixel}")

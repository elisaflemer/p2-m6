# Exercício prática | prova 2, módulo 6

Esse repositório contém a solução para o exercício prático de detecção de faces em vídeo. Ele cumpre três funções:

1. Identifica faces em um vídeo de entrada
2. Desenha um retângulo em volta da face identificada
3. Salva o vídeo de saída com o retângulo desenhado apenas nos frames em que faces foram identificadas

A implementação desse exercício foi feita utilizando OpenCV com Haar Cascade nativo da biblioteca. Para isso, foi utilizado o arquivo `haarcascade_frontalface_default.xml`, do OpenCV. 

Na pasta "codigo", há dois scripts que realizam toda a operação em dois vídeos: um dado pelo enunciado e outro gravado durante a prova. Como o vídeo original apresentou uma performance ruim com o modelo, com muitos falsos positivos, foi gravado outro vídeo para explorar o programa, dado que não houve tempo durante a avaliação para refinar o modelo.

Nesse sentido, cada script carrega o Haar Cascade e o respectivo vídeo de entrada. Então, cria-se o arquivo de vídeo de saída no mesmo tamanho do vídeo de entrada. Feito isso, passa-se por cada frame do vídeo, aplica-se o filtro de escala de cinza e o Haar Cascade. Quando faces são detectadas, retângulos são desenhados ao redor delas. Da mesma forma, frames com faces são adicionados ao vídeo de saída. Por fim, mostramos o frame atual, independentemente de faces terem sido identificadas ou não, na interface gráfica do video player.

Os vídeos de saída são salvos em "out_videos".
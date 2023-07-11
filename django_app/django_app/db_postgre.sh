docker run --name postgre_container \
    -e POSTGRES_PASSWORD=mot_de_passe \
    -e POSTGRES_USER=utilisateur \
    -e POSTGRES_DB=postgre_db \
    -v /home/apprenant/Documents/projets/Realiser_un_site_d-analyse_de_sentiments/postgre_local \
    -p 5432:5432 \
    -d postgres
docker run --name postgre_container \
    -e POSTGRES_PASSWORD=mot_de_passe \
    -e POSTGRES_USER=utilisateur \
    -e POSTGRES_DB=postgre_db \
    -v /home/apprenant/Documents/projets/Realiser_un_site_d-analyse_de_sentiments/postgre_local \
    -p 5433:5432 \
    -d postgres

#############
# commands: #
#############
# docker stop b2b5457ed6a3              to stop a container
# docker system prune                   to delete all
# sh db_postgre.sh                      to create a new container
# python manage.py makemigrations       to makemigrations of the new postgresql table
# python manage.py migrate

# To execute the docker
# docker exec -it 0c34b2442a04 bash   
# To connect to postgresql  
# psql -U utilisateur -d postgre_db  
# To show all tables  
# \dt       
# To show a specific table                            
# \d nom de la table                    
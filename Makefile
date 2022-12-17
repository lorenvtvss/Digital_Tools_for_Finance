run in terminal:
        1. 
	docker build -t dtffprojectjn -f Dockerfile .

	2. 
        # docker run -it --rm --name dtff-project-jn-container -p 10000:8888 -v "${PWD}":/home/jovyan/work dtffprojectjn 
	docker run -it --rm --name dtff-project-jn-container -p 10000:8888 dtffprojectjn 
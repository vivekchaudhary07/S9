curl --location --request POST 'http://localhost:8080/2015-03-31/functions/function/invocations' \
--header 'Content-Type: application/json' \
--data-raw '{
    "body": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAAAAABXZoBIAAAAzElEQVR4nGNgGMxAtOV/Ay65iLt//34xwC7n+evvzLq/lwKxSh7528ng/Of2V1Msci6//2oyMGTG/fXAZurfN7JAagEOyTsiDAyq396rYZE0//a3XZIh7+9RrA6K+ft3qfOrvwpYJdk3/QWC42xYJRl4gYHwNxi7HAMDJ1CyCpekFlDyBQ8OyfN/97z7645dTvfTDX6PvwexynHM+ZsLNHk1VkmBv3+TpHv+lmOVzPr7e+qLvxfFsUpWAN36fDN2OQa/y8umGmKXoi4AAKaKWJZgAVknAAAAAElFTkSuQmCC"
}
'
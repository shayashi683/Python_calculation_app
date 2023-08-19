from modal import Image, Stub, web_endpoint, Mount

stub = Stub("deployment-16885")

image = Image.from_dockerfile("Dockerfile.modal", context_mount=Mount.from_local_dir(".", remote_path="/"))

@stub.function(image=image, memory=1024, cpu=2.0)
@web_endpoint(label="deployment-16885")
def primary_function():
    import main
    return main.main()
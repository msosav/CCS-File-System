# Comandos útiles

## Generar requirements.txt

Es necesario estar en el entorno virtual

```bash
pip freeze > requirements.txt
```

## Generar servicios de gRPC

```bash
python -m grpc_tools.protoc -I ../protobufs --python_out=. --pyi_out=. --grpc_python_out=. ../protobufs/Service.proto
```





ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FML3JFV%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T002611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDwIl3RUvduS%2BdYyLOhulC%2Fur%2FOnNxSFHNRAakEZvt%2F8AiAqkDdsuLiEx8bwbvxe7pU2Y939jWTy3LZ1FUiklVHcRCr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMWdfYyjuVghgwt5B%2FKtwDJtKew72AK2OA0Jflihv8Dijiu0fl8xrBIJelc03gk2R78HmJOz5DXHc%2BVAH%2FVdEDDMyRCPy2E71SmJbfAD%2B5%2F1hbRKk3hCNi84j0xFjzya%2Fbz2eLhRK6JULQROkIzLdbex1I2urT%2B3cGUe2MJYXkVoXH1UGNWf0NJelsrztLJt4OV2mVRKAtj8CIgjoVgsjdAx8dCOSHEOafnH8yb9lTvMJ6edtA2XsMD7mKNysDdxuylVnFpdn085M8Gya2d7To7zNPFSO8BzFhbmf6Vc29eREvE7Rj5L%2FerjEyQ72f8%2Bs%2BfZ2jKlWwUSMw3YMncQsLW9HoU2LkyJbjrpAW%2FRAdWH8C%2FM9Bu%2BIoc5EhjCumNmZAepdmGJdgils%2FCiKMQ6c3lFTpnPLt5U1R8pN4HVX%2Fk%2BVpIi3cK0RdJXunZDv3wNeugbOGLqZhaHTv3NULOWaj8BN4veZGQFVuI%2FFdaX9mrIg3VNQkxvSJcnIYucJpe3nBONVSe5w8omksq44lXyd%2BVdqXLvq9r27GYdcFexf1m7unna8%2FL6m%2FcU5m8FX57ZjaoeHm%2B%2FcWmZjl98T0Y8P6MeEOF0h2ZvFEUvcpBSuEfhmPbLYcgIaFZCBu7zFcXNOmaQQXSw0OD71pBi4wip%2F21QY6pgE6mLvVXTAVCSy7qQbWYMfJrK7333AmZOwMNiNoT%2B5Feik%2FRxCN8I9EUAlqaIugSAtF0fjrUXttraAlkOXOvJBG2n0Ss4A8UY4Q3TshZvQJG7li1D1E%2FeIqBbMSW4C%2BjLLfDS1WDfeAmCPBJcpxo4kqKM%2BCKnCT9FkumwjsquoE8e5xOAVFXyE1OzsHRi9zzbR55LZCxP7j049ZhqTgX6IzX0MU8nv2&X-Amz-Signature=adb0d381400fb180bdab3c4dfc471b62e85e8298477760fd0c8fb17effb28add&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FML3JFV%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T002611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDwIl3RUvduS%2BdYyLOhulC%2Fur%2FOnNxSFHNRAakEZvt%2F8AiAqkDdsuLiEx8bwbvxe7pU2Y939jWTy3LZ1FUiklVHcRCr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMWdfYyjuVghgwt5B%2FKtwDJtKew72AK2OA0Jflihv8Dijiu0fl8xrBIJelc03gk2R78HmJOz5DXHc%2BVAH%2FVdEDDMyRCPy2E71SmJbfAD%2B5%2F1hbRKk3hCNi84j0xFjzya%2Fbz2eLhRK6JULQROkIzLdbex1I2urT%2B3cGUe2MJYXkVoXH1UGNWf0NJelsrztLJt4OV2mVRKAtj8CIgjoVgsjdAx8dCOSHEOafnH8yb9lTvMJ6edtA2XsMD7mKNysDdxuylVnFpdn085M8Gya2d7To7zNPFSO8BzFhbmf6Vc29eREvE7Rj5L%2FerjEyQ72f8%2Bs%2BfZ2jKlWwUSMw3YMncQsLW9HoU2LkyJbjrpAW%2FRAdWH8C%2FM9Bu%2BIoc5EhjCumNmZAepdmGJdgils%2FCiKMQ6c3lFTpnPLt5U1R8pN4HVX%2Fk%2BVpIi3cK0RdJXunZDv3wNeugbOGLqZhaHTv3NULOWaj8BN4veZGQFVuI%2FFdaX9mrIg3VNQkxvSJcnIYucJpe3nBONVSe5w8omksq44lXyd%2BVdqXLvq9r27GYdcFexf1m7unna8%2FL6m%2FcU5m8FX57ZjaoeHm%2B%2FcWmZjl98T0Y8P6MeEOF0h2ZvFEUvcpBSuEfhmPbLYcgIaFZCBu7zFcXNOmaQQXSw0OD71pBi4wip%2F21QY6pgE6mLvVXTAVCSy7qQbWYMfJrK7333AmZOwMNiNoT%2B5Feik%2FRxCN8I9EUAlqaIugSAtF0fjrUXttraAlkOXOvJBG2n0Ss4A8UY4Q3TshZvQJG7li1D1E%2FeIqBbMSW4C%2BjLLfDS1WDfeAmCPBJcpxo4kqKM%2BCKnCT9FkumwjsquoE8e5xOAVFXyE1OzsHRi9zzbR55LZCxP7j049ZhqTgX6IzX0MU8nv2&X-Amz-Signature=a9f74fda3f44e705eb4061bf02b9dedfd40e6899ea0d79df5385ff92df441a18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test








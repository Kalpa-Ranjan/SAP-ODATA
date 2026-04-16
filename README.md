



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O2X6QWR%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T190511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxXcH8IuCeC7vekT9UjR5trPHF57XQu0YerHHucxg5BQIgTV9GM%2FGAOMnV6FRdnifFT5MX7YlA9NbXgbEDNgIqUpQqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLlj%2Ff9Q4rcOI9PflSrcA7EZTSHDemvkXJVOydeYD7Rm6RQcFpGeyNYCewjKijBxZCeu33vOQjJn8qlo%2F%2BWavyQSK6hq2HFxq5EPezNOmU7s9akbV8NVGEv7ax1OjJXQ4rN9s1OdTYJilvioerYELUXqSlxvK%2Fp4Sj%2BKuGULDGF%2B3R13KMt39CnLeRe%2FmQOsxSK4yHpUciRsQuQPKBFSKJk%2BwdHoTAzvXkjbbxNORfhFUlg8YC5rU6BXuQPok0qibdliFSJFOB3bJSiHz3SjeF2aGz21RL%2BqJC66on6uPVvr5T4QRqBiJv5%2FmqjDl0RN1B6h3vUguV%2BZzjGd7sg7whaVFe17yghD34oMtrk2JlzJrvCFC%2Bleq994e0mDB9lQtgc1RPBLsWb5RNWIVc8wF0OP3vI7ciABno8TyKmtVrvjQAj1jGSaEJ%2Fq9LhVtXpzD3o3vNSTYdZrAotrdhJQm9uultRtgkxrjk%2B%2Bunjyjan361XXz4K64IhVI3drcabk8YzmKTz%2FUrOwGEjoKNH8qU9%2FRabun7CZk4AqSZgljK0BD2JSzt3gp%2BZ%2BeQvze87W0PDHeyO2O%2BIF9gJ9RTvkDScJtRwyk1ExRI5rmeqlNZ3gy4nCJyzA2BKDB%2Fpj8IAWOW2nFAwTF%2FWZQEXFMN7ehM8GOqUB6og9G3R3IXVe6QNiWbJQLL84Dc9LvZr51L%2FNNeW479u%2FwYZ9oga65KZezKIG2G5luNz06dw9uf7d00lDs7uL5%2Fwaf03d%2FO7W8CNOmnLfyp7LD66d9gqZlRte9AhArfj%2BFbgELVqQymdaVqu4PQ5YYKSLbHkJyK4nzw7JuyCePItTog5tfm%2BSd%2FvwUbaA4fTDKNmuxrpR3IVjr8iSdWt8oG7QOvLq&X-Amz-Signature=43165eb5c0e10e15a8e27995f25bb6d974e3e6308ddb26e04d9189b96c1f6856&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O2X6QWR%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T190511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxXcH8IuCeC7vekT9UjR5trPHF57XQu0YerHHucxg5BQIgTV9GM%2FGAOMnV6FRdnifFT5MX7YlA9NbXgbEDNgIqUpQqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLlj%2Ff9Q4rcOI9PflSrcA7EZTSHDemvkXJVOydeYD7Rm6RQcFpGeyNYCewjKijBxZCeu33vOQjJn8qlo%2F%2BWavyQSK6hq2HFxq5EPezNOmU7s9akbV8NVGEv7ax1OjJXQ4rN9s1OdTYJilvioerYELUXqSlxvK%2Fp4Sj%2BKuGULDGF%2B3R13KMt39CnLeRe%2FmQOsxSK4yHpUciRsQuQPKBFSKJk%2BwdHoTAzvXkjbbxNORfhFUlg8YC5rU6BXuQPok0qibdliFSJFOB3bJSiHz3SjeF2aGz21RL%2BqJC66on6uPVvr5T4QRqBiJv5%2FmqjDl0RN1B6h3vUguV%2BZzjGd7sg7whaVFe17yghD34oMtrk2JlzJrvCFC%2Bleq994e0mDB9lQtgc1RPBLsWb5RNWIVc8wF0OP3vI7ciABno8TyKmtVrvjQAj1jGSaEJ%2Fq9LhVtXpzD3o3vNSTYdZrAotrdhJQm9uultRtgkxrjk%2B%2Bunjyjan361XXz4K64IhVI3drcabk8YzmKTz%2FUrOwGEjoKNH8qU9%2FRabun7CZk4AqSZgljK0BD2JSzt3gp%2BZ%2BeQvze87W0PDHeyO2O%2BIF9gJ9RTvkDScJtRwyk1ExRI5rmeqlNZ3gy4nCJyzA2BKDB%2Fpj8IAWOW2nFAwTF%2FWZQEXFMN7ehM8GOqUB6og9G3R3IXVe6QNiWbJQLL84Dc9LvZr51L%2FNNeW479u%2FwYZ9oga65KZezKIG2G5luNz06dw9uf7d00lDs7uL5%2Fwaf03d%2FO7W8CNOmnLfyp7LD66d9gqZlRte9AhArfj%2BFbgELVqQymdaVqu4PQ5YYKSLbHkJyK4nzw7JuyCePItTog5tfm%2BSd%2FvwUbaA4fTDKNmuxrpR3IVjr8iSdWt8oG7QOvLq&X-Amz-Signature=3dc1ff7301c08604f7c756ada64c5761c311ea77c633d56665992d1b6d691b3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








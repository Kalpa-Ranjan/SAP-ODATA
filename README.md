



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S545NQRV%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T021016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhUZ9f1gWudTWJInrGYKMFzJDvG3PhFOq7YYt8%2B%2BHxQAIhAP9THKnDngeYlBpjjYI8Ci1lIp3IUBGnF8C1KZNlyjFxKv8DCHYQABoMNjM3NDIzMTgzODA1IgyA6fm6Lcuarp8BH5Iq3AODKV6n1wvlCqeN8%2B1gQgWZW06NgK6ZWcxLKFvYj2Ev6cSUoBdJ0ggEIle3vmgNfXPIRRWQ5ZN7y%2FUhOVHFIbiHyu6bfaARHu3EQwM6%2FZIMTUiJ9P7o0vPMNX36xUPQzDaUAHzwag1y%2F%2FEDwBFjnDRVw8t4vBVqB1cZuhakALKCZOsXAnoCkdp94pT%2FhYyGdAgjCVEYevubJeQdNsZoAvcxfXL2lRi24mPHeOB7ltgJNRgx6dDhRvXO1OOAx41xaT%2FObRkm4Z79edpliWjL1DKvaPcdF8vj06JRjkMpwpxBTheMVqQdQnaAh4EJ%2FB%2FVBw5qxkBajUm%2FKIeXv8PU%2B5Bj9cwKgsyS7Iad%2Bb2MDN2ggXuj6TElS4ROr3LlNYbNny%2BHGhIILw9Bsp5MTgEdObbuIYi29lm68elyMM6l6R1rngl7szPjSLKdcuH41AaFeUqVB%2FhVUCrQZ2qCGVSM9cvcKrWQPARBT7lgWSbYzea4IuNuwqw1wk1cD4R3Cpmx0Q5eRVOr7l3t3skOZsUOyRGh3bOxsu4xJ0BX7Xx0vqL5z3Ur7ojhwHJvO76604opk781iIHaZo8dZ2Vm1CIs2zj7R0aX6qmSmDzVOe%2Bcwowje4YAcvLuBDyAXT7mNDCdy7XSBjqkAfC7gQduFDgKnKteDG6eUT0HIHYUXyqxuomaKE6eJzis6pKOMPUtS8cI%2FRc9n5oelqXPQBEGm1TecDpInsnJGt49Iak8j3wKaDeY%2Fpz4ao7GPshRuYcdgQtN0NdbqkexUg9fjdjvZYhX%2BYnBLHXV2Q25PucfLb5mPgRSJ%2FaKq5sBj0qAFC8qpvZyITj2Am6l0pAKmFrmvKDjsNmRmFDZBSX8erEN&X-Amz-Signature=a1d8f98e24c1e124a80c0887c4e665397c37d557d5eaf764ecae1693fee03f6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S545NQRV%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T021016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhUZ9f1gWudTWJInrGYKMFzJDvG3PhFOq7YYt8%2B%2BHxQAIhAP9THKnDngeYlBpjjYI8Ci1lIp3IUBGnF8C1KZNlyjFxKv8DCHYQABoMNjM3NDIzMTgzODA1IgyA6fm6Lcuarp8BH5Iq3AODKV6n1wvlCqeN8%2B1gQgWZW06NgK6ZWcxLKFvYj2Ev6cSUoBdJ0ggEIle3vmgNfXPIRRWQ5ZN7y%2FUhOVHFIbiHyu6bfaARHu3EQwM6%2FZIMTUiJ9P7o0vPMNX36xUPQzDaUAHzwag1y%2F%2FEDwBFjnDRVw8t4vBVqB1cZuhakALKCZOsXAnoCkdp94pT%2FhYyGdAgjCVEYevubJeQdNsZoAvcxfXL2lRi24mPHeOB7ltgJNRgx6dDhRvXO1OOAx41xaT%2FObRkm4Z79edpliWjL1DKvaPcdF8vj06JRjkMpwpxBTheMVqQdQnaAh4EJ%2FB%2FVBw5qxkBajUm%2FKIeXv8PU%2B5Bj9cwKgsyS7Iad%2Bb2MDN2ggXuj6TElS4ROr3LlNYbNny%2BHGhIILw9Bsp5MTgEdObbuIYi29lm68elyMM6l6R1rngl7szPjSLKdcuH41AaFeUqVB%2FhVUCrQZ2qCGVSM9cvcKrWQPARBT7lgWSbYzea4IuNuwqw1wk1cD4R3Cpmx0Q5eRVOr7l3t3skOZsUOyRGh3bOxsu4xJ0BX7Xx0vqL5z3Ur7ojhwHJvO76604opk781iIHaZo8dZ2Vm1CIs2zj7R0aX6qmSmDzVOe%2Bcwowje4YAcvLuBDyAXT7mNDCdy7XSBjqkAfC7gQduFDgKnKteDG6eUT0HIHYUXyqxuomaKE6eJzis6pKOMPUtS8cI%2FRc9n5oelqXPQBEGm1TecDpInsnJGt49Iak8j3wKaDeY%2Fpz4ao7GPshRuYcdgQtN0NdbqkexUg9fjdjvZYhX%2BYnBLHXV2Q25PucfLb5mPgRSJ%2FaKq5sBj0qAFC8qpvZyITj2Am6l0pAKmFrmvKDjsNmRmFDZBSX8erEN&X-Amz-Signature=bc8e9e21b086c9d5b104f2708511676c57242f7243f553624f4cc7494c3346bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








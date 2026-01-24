



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXPWS5VL%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T123147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJIMEYCIQCksc9COGgG0fT8l3kpcFA3mBk1KlvqKfMwFr0oV%2FOO0wIhANZOdjjHyUmV4fUQ3iK70%2B9OjyRd4IjNMNP23NvyWMJ6Kv8DCA0QABoMNjM3NDIzMTgzODA1IgwY0dADzwoOd98UJZQq3AOHrpEeGrdMRvzuqwQ5hQHEcJzHfLUVqE1Jyoo2daKFlkxxVy311%2B%2Fyv4U5gXljESocOiEIi0LBnPiMqfmE0PeTG%2FiemiYmQlYF9Zi8ongfEcznmiXiGnix4mH1oqs9lRsU2pozVKPzX4GFLmyDLmAENvM44bkPlN2qiIM%2BFVWcLIXPfN8tGapva8EkRsOLiyKaB1%2BXzFe17S9vN2ygBCrYBfAh60IyfTBLEdULz5eSv5PIx0PrpgayR0h92sFy3aXl3msB81orDiGRJhlu%2BEhngUsDOqchp1H568nTu1oTYa3%2F%2FOHkU%2B2TtbiUiyYTx14RdpA60R1i8ncM5nSpxnNZVrI5RgWzQwdGgjGPFst81H1OLW6dscp5DB92aHqpaD1bM3VHYBkF1vIUC7Ln17Ndn0t5kbxqB3IrtdJl7nhy8%2F0yf5Al5hGRurLp1YNJ8k2ieAXQAAi7cFgKYLlerosAuoyPE3zR1cLxS5O9OdwVBFk0Y%2BAzDn7Q05EsutFjK6X%2B0vvqvnWYHzxvSPSSzjSmFNMabXV7YdwzJp4ZOBoUYEhGs8gS5inazLMzigth%2FGa77PHo15ySyIrRBlaIRD2GH3CNvi0BZCmbqkPDnZV3j27qWry68TTtxq5fKzCq8tLLBjqkAaGLxPMfFO9j7Rv%2FgqaMFtbBul0eQmt%2BI%2BvUkU1jwVDDNhMmIhQNBjGPQyetSppHnhFiU71pRIp3vkI0YO%2FK9DcOy3f%2FEr%2BvwOzGF2G%2B4%2FhA4hI4wqN17zh0n5vjYXylTW8g383WxYc3ITTyKdphTGvy1AGJvz%2FsC8L40rWctFfYINjZTOUeQ1NnKuClfYycP%2BsJ4%2FoGg3sXzyLOpJrO9t9iamOV&X-Amz-Signature=3c3844f2e0e641fc2383a86ae98904b01e9f57353668fd2645f86c7ac9f235d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXPWS5VL%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T123147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJIMEYCIQCksc9COGgG0fT8l3kpcFA3mBk1KlvqKfMwFr0oV%2FOO0wIhANZOdjjHyUmV4fUQ3iK70%2B9OjyRd4IjNMNP23NvyWMJ6Kv8DCA0QABoMNjM3NDIzMTgzODA1IgwY0dADzwoOd98UJZQq3AOHrpEeGrdMRvzuqwQ5hQHEcJzHfLUVqE1Jyoo2daKFlkxxVy311%2B%2Fyv4U5gXljESocOiEIi0LBnPiMqfmE0PeTG%2FiemiYmQlYF9Zi8ongfEcznmiXiGnix4mH1oqs9lRsU2pozVKPzX4GFLmyDLmAENvM44bkPlN2qiIM%2BFVWcLIXPfN8tGapva8EkRsOLiyKaB1%2BXzFe17S9vN2ygBCrYBfAh60IyfTBLEdULz5eSv5PIx0PrpgayR0h92sFy3aXl3msB81orDiGRJhlu%2BEhngUsDOqchp1H568nTu1oTYa3%2F%2FOHkU%2B2TtbiUiyYTx14RdpA60R1i8ncM5nSpxnNZVrI5RgWzQwdGgjGPFst81H1OLW6dscp5DB92aHqpaD1bM3VHYBkF1vIUC7Ln17Ndn0t5kbxqB3IrtdJl7nhy8%2F0yf5Al5hGRurLp1YNJ8k2ieAXQAAi7cFgKYLlerosAuoyPE3zR1cLxS5O9OdwVBFk0Y%2BAzDn7Q05EsutFjK6X%2B0vvqvnWYHzxvSPSSzjSmFNMabXV7YdwzJp4ZOBoUYEhGs8gS5inazLMzigth%2FGa77PHo15ySyIrRBlaIRD2GH3CNvi0BZCmbqkPDnZV3j27qWry68TTtxq5fKzCq8tLLBjqkAaGLxPMfFO9j7Rv%2FgqaMFtbBul0eQmt%2BI%2BvUkU1jwVDDNhMmIhQNBjGPQyetSppHnhFiU71pRIp3vkI0YO%2FK9DcOy3f%2FEr%2BvwOzGF2G%2B4%2FhA4hI4wqN17zh0n5vjYXylTW8g383WxYc3ITTyKdphTGvy1AGJvz%2FsC8L40rWctFfYINjZTOUeQ1NnKuClfYycP%2BsJ4%2FoGg3sXzyLOpJrO9t9iamOV&X-Amz-Signature=8ad549576d7741a65893c94060867c46f212c9ffc7db4851de1808ef5954b747&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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












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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ7NWYLB%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T130130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF8fqnmbLQ2t2mbyoiItBktxQjdy6jztSPRF6xEGln2CAiEAsLklvBLex0XO5XQXdI2Dm7d6ajF7Qr%2FBaWf31%2Bfnpp0q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDJIozKml1KP4CEgcdyrcA8Jva7roQT6wP0%2B6wfzIEz0jnjCO5kZypfCfMcj9q48SVROEZ2dUix8KkSaC9zOnj5%2BuMSMclYDhdGD1DaE8mtulI7MO97jFbGUa7txX4VM8%2FSu%2FE9WX6gSK0ToSylnfcmDqKuKCLIlZGBB%2B1TVNgkTuGVw3rAuvYoAUUgSwYDx2Q2hstYlwmWctpJf%2F9MDzuTqK7ebBRSZhqfzDougutJ2i5cvH4bfWl1L8GcO3IiPtgVO9RZov1Bw7UEW9uWdbuRsn2%2BPL9eipk59CtyylgTZ1tp2Gba54%2FrTzat3Dl%2F0PONKgfM8%2FH6FYYXtRULR346EWczAQ3nYkk070JTZw%2BOtG2hf46tO9rXD%2BYZsizJakg9jYPZl5l%2Be7C6fDM5JxA%2BtFSYlOqq9gAc7teik5L%2B%2B7PJMi1RfNIcMsSHrLD%2BURlDE4mx2r%2Brn5AmoybtvWYOnBCkbWe63YM48LND1Yf8yyyAY4j77ditdqaShsvjEUCLRXEkaqn5KbUsKG8uzQaDDylB8rWrCk6wPqdt2fCuNkMNF5vRJCbZs9dyijok%2BgHJ5GhwgFKGvYaFWrBj2hCQJkwzM6H8ea0WKu4A7mmN0M6655500DDEAtZK%2BHcTwkZdD9cfN7RkpTG1%2BHMOSguc4GOqUBP2TxhXLDMxAxfLsI1Ws8zK4xQlN2VEQvvvKiMye9eVaQLwsquUPTeuiFZB0I4Ue4QlxTPblr1yz9CVSbay07O6CgvnMpTMLqugpAfJf7jim8ieRpjRFLSMGOgG%2B%2F5v2Z4s58A0jdRz82ZVqVXCqsGLdCd8KTUH4htnordDqH0NStToIFbGErzzqqlAYz9DcMWOQeUJUw%2F8FZp5v5QnlDaSTuLaE8&X-Amz-Signature=5bbd5998099713d6fade604ba96e392d5237b076d35713eaa1c0331b9a8768c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ7NWYLB%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T130130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF8fqnmbLQ2t2mbyoiItBktxQjdy6jztSPRF6xEGln2CAiEAsLklvBLex0XO5XQXdI2Dm7d6ajF7Qr%2FBaWf31%2Bfnpp0q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDJIozKml1KP4CEgcdyrcA8Jva7roQT6wP0%2B6wfzIEz0jnjCO5kZypfCfMcj9q48SVROEZ2dUix8KkSaC9zOnj5%2BuMSMclYDhdGD1DaE8mtulI7MO97jFbGUa7txX4VM8%2FSu%2FE9WX6gSK0ToSylnfcmDqKuKCLIlZGBB%2B1TVNgkTuGVw3rAuvYoAUUgSwYDx2Q2hstYlwmWctpJf%2F9MDzuTqK7ebBRSZhqfzDougutJ2i5cvH4bfWl1L8GcO3IiPtgVO9RZov1Bw7UEW9uWdbuRsn2%2BPL9eipk59CtyylgTZ1tp2Gba54%2FrTzat3Dl%2F0PONKgfM8%2FH6FYYXtRULR346EWczAQ3nYkk070JTZw%2BOtG2hf46tO9rXD%2BYZsizJakg9jYPZl5l%2Be7C6fDM5JxA%2BtFSYlOqq9gAc7teik5L%2B%2B7PJMi1RfNIcMsSHrLD%2BURlDE4mx2r%2Brn5AmoybtvWYOnBCkbWe63YM48LND1Yf8yyyAY4j77ditdqaShsvjEUCLRXEkaqn5KbUsKG8uzQaDDylB8rWrCk6wPqdt2fCuNkMNF5vRJCbZs9dyijok%2BgHJ5GhwgFKGvYaFWrBj2hCQJkwzM6H8ea0WKu4A7mmN0M6655500DDEAtZK%2BHcTwkZdD9cfN7RkpTG1%2BHMOSguc4GOqUBP2TxhXLDMxAxfLsI1Ws8zK4xQlN2VEQvvvKiMye9eVaQLwsquUPTeuiFZB0I4Ue4QlxTPblr1yz9CVSbay07O6CgvnMpTMLqugpAfJf7jim8ieRpjRFLSMGOgG%2B%2F5v2Z4s58A0jdRz82ZVqVXCqsGLdCd8KTUH4htnordDqH0NStToIFbGErzzqqlAYz9DcMWOQeUJUw%2F8FZp5v5QnlDaSTuLaE8&X-Amz-Signature=729168729632dc17349b8fc44500f832fb70587ab3c999c5dc8fba0589415fdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








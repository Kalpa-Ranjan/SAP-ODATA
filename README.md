



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTK2YGYL%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T185854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDGtHZF05%2Bh7OjI4EoDlR%2Bkre1XJvKaFM0rFUtkvbt4EQIhAJWj0XkNihKboghiaccvnznsY2j2iJ4RV3FkyjhZyWJuKv8DCBMQABoMNjM3NDIzMTgzODA1IgzsabefAMYh%2B6WQ4Y0q3ANZZzKRufeMTqRcS3S0ODAKnOG0A5xdS1JSRsi%2B7qjBXflqJWUmxMtbNXbzHzQgwRrZMqslzx4ReqUXfoOlaUEb8T0wfaNOg0sWk0Ny9UkCSHmpWIioQXvzn9RfyGsWDXPuBVDgAHqcQ1ZifONGfbRXlAX%2B2pcCeW1nyGdFgOXAubQJNdZ5o1NIWaJMFisqbpfgYfpNuUCisNBDpqbNWegUy5fa4Lp0R%2BiCw2Nl4azYGx2SJO7TMHplrkBdPwZKhyzwawaysBPRSNz07zz0d88Y0UL03SIJUszJtFa1H0xFpoywgJWYCQxZyZJlU3BsmmheyRYaC6BYKgNl32pgt7g3%2BUL8mbRc54uEAmmnQjXgcPeF%2BdDatjcajUo22vEScypfZq9O%2F9A5CEsmfwspNPVrkk6wQEsSw1ePCRnlPpE5zgIMoJG37bXQKZUWw1RuFyvF6sw8jgFCd2epJTSaQgFztt6cd%2BUEid7IKH99t3XT2WBdY1kWPc3h7g2SwquB5YmMJM8pq3Vr34WsqUBklrrMvzcAAPdVeK5Nt1jBiMHTJyEJkjT%2Fk97IF6EQUr3gFfAW6tj1R9cIOLoqI9%2FmrZQJ%2BmCmYaFp2x2wXWKT7p%2BzS2CiMLl9cxFAiwVo7TCX9%2FzMBjqkAbQ1HDLy3%2BTLVR%2BMIx9oCYjqpZe8b%2BKH79tYx7oVOPkrDOo%2FQt04%2FJkQBgHsZVqWyjyT1WOHViHYr2neR3Y67EkV9kK6auHMzytX7gqnRLweKV%2Ffq5xSnP7%2BOEb2zbpINzIIqyEzI0pfaDQbGoANysj%2BQO%2FuhrdQl5XClinzKT45o43i73S3H9cYAQpe6Ok95Zfuo92qncu6nW5PiIM4yFZj9eSY&X-Amz-Signature=2dfd99e08f74770c1dcae274ac97e0b9f41a6789a3941c81479a7075f504425d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTK2YGYL%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T185854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDGtHZF05%2Bh7OjI4EoDlR%2Bkre1XJvKaFM0rFUtkvbt4EQIhAJWj0XkNihKboghiaccvnznsY2j2iJ4RV3FkyjhZyWJuKv8DCBMQABoMNjM3NDIzMTgzODA1IgzsabefAMYh%2B6WQ4Y0q3ANZZzKRufeMTqRcS3S0ODAKnOG0A5xdS1JSRsi%2B7qjBXflqJWUmxMtbNXbzHzQgwRrZMqslzx4ReqUXfoOlaUEb8T0wfaNOg0sWk0Ny9UkCSHmpWIioQXvzn9RfyGsWDXPuBVDgAHqcQ1ZifONGfbRXlAX%2B2pcCeW1nyGdFgOXAubQJNdZ5o1NIWaJMFisqbpfgYfpNuUCisNBDpqbNWegUy5fa4Lp0R%2BiCw2Nl4azYGx2SJO7TMHplrkBdPwZKhyzwawaysBPRSNz07zz0d88Y0UL03SIJUszJtFa1H0xFpoywgJWYCQxZyZJlU3BsmmheyRYaC6BYKgNl32pgt7g3%2BUL8mbRc54uEAmmnQjXgcPeF%2BdDatjcajUo22vEScypfZq9O%2F9A5CEsmfwspNPVrkk6wQEsSw1ePCRnlPpE5zgIMoJG37bXQKZUWw1RuFyvF6sw8jgFCd2epJTSaQgFztt6cd%2BUEid7IKH99t3XT2WBdY1kWPc3h7g2SwquB5YmMJM8pq3Vr34WsqUBklrrMvzcAAPdVeK5Nt1jBiMHTJyEJkjT%2Fk97IF6EQUr3gFfAW6tj1R9cIOLoqI9%2FmrZQJ%2BmCmYaFp2x2wXWKT7p%2BzS2CiMLl9cxFAiwVo7TCX9%2FzMBjqkAbQ1HDLy3%2BTLVR%2BMIx9oCYjqpZe8b%2BKH79tYx7oVOPkrDOo%2FQt04%2FJkQBgHsZVqWyjyT1WOHViHYr2neR3Y67EkV9kK6auHMzytX7gqnRLweKV%2Ffq5xSnP7%2BOEb2zbpINzIIqyEzI0pfaDQbGoANysj%2BQO%2FuhrdQl5XClinzKT45o43i73S3H9cYAQpe6Ok95Zfuo92qncu6nW5PiIM4yFZj9eSY&X-Amz-Signature=1a5f274cfebbca43248cf3bf839ed7ccc7c6f71b4ebc407af61a8d69de5f2bc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








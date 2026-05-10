



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2LLEY7%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T080158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJIMEYCIQD1AsmrFRUwD%2F%2BnEl%2B0bb%2F4iRjSAFVD4QK3F0Gr6ao3HQIhAMqT%2FU%2FNfb9AtvjtGVA%2BfnqqDhXvKFoZ2gdWFcTOCVL6KogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4jLF6ImR2Y6ekKUq3APp0%2BsvpYQ1le8CzpzEfLULQGr6l42jfW6lmx3T%2BexytyrbPMMpFDlBhRF06EcoF3hMRzRCBAEk0f6JLQ5JhOVeOybOxVhKBSn9XlCqMnQNmp%2F8QVlr9%2FxBgvZ94wRhL6LavXFVsXof1g%2BHQTCPcyOvkdAd%2BrT6UXeNx1mU3si7ZrDGnj1ZVcck6z76NUk%2FeV7WHZVhS1MZsMiqSL5YzF%2Fd58a8s2KS8IB0Zy0vxMeX9EcWyi2kLrvb9sqCZHk6T9crwdhK5p%2BOY85GHLBeTPTMlEvf%2Fx2kGBoa2LOUeO4V0H5S2qOYcfQHbydhvd9hJTWOMaRxWygw7KehcjRvFQeE4G0ppnCs667PdOC5oU%2Bt8x9FpMTEsE%2BnF0iTovXZZxQGW%2FB8Gmq0Y51lYOxWcuIxRBoEGZxFTPUFpWbNxv9RtNF6xVQRn8rSYeq65Q%2FFJkOXLesE25u2ooyLdhw3zCaGWHrtXPO5f9ObatQ3I6Sklec36iUTyizi90EktsYSnq8sdi4vCv0eQc%2F2%2FC%2BPDy551O292Gjpqw6IODdgVEtQHlyRYFBmklshk%2FpxEKsOUjOO1WFhPjQETufX3lJWDmHn9BetmwikZ%2FVbEm%2B83SlvmpAqk2mvBYubkIZLNDD3koDQBjqkAfvwVdgYY%2Bwa%2FLHwdUCU%2F6oYlUzZ5JJIBvmPimSvPL0dwHGYrMkknU4Ei5puNFvjqIdA1V5SQkx0Ynl7%2Boi1ZSH4YucwQKEE3pMrP1sDU70TTgqP%2FsCD%2FxHL9HwR%2FOwmHoPjwrx49mkn%2FeRzv3TXHQ0dhrcdztIWuHdZ1hmtGFK9x%2B8CohbdRYaDUC9lEj%2B2uePdV%2FmXGC3IMtBkEM1HUbDehroJ&X-Amz-Signature=54c92de0f46db1bdd68b3cacc427324cd3a95137b808b22f85987f6d59386846&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2LLEY7%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T080158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJIMEYCIQD1AsmrFRUwD%2F%2BnEl%2B0bb%2F4iRjSAFVD4QK3F0Gr6ao3HQIhAMqT%2FU%2FNfb9AtvjtGVA%2BfnqqDhXvKFoZ2gdWFcTOCVL6KogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4jLF6ImR2Y6ekKUq3APp0%2BsvpYQ1le8CzpzEfLULQGr6l42jfW6lmx3T%2BexytyrbPMMpFDlBhRF06EcoF3hMRzRCBAEk0f6JLQ5JhOVeOybOxVhKBSn9XlCqMnQNmp%2F8QVlr9%2FxBgvZ94wRhL6LavXFVsXof1g%2BHQTCPcyOvkdAd%2BrT6UXeNx1mU3si7ZrDGnj1ZVcck6z76NUk%2FeV7WHZVhS1MZsMiqSL5YzF%2Fd58a8s2KS8IB0Zy0vxMeX9EcWyi2kLrvb9sqCZHk6T9crwdhK5p%2BOY85GHLBeTPTMlEvf%2Fx2kGBoa2LOUeO4V0H5S2qOYcfQHbydhvd9hJTWOMaRxWygw7KehcjRvFQeE4G0ppnCs667PdOC5oU%2Bt8x9FpMTEsE%2BnF0iTovXZZxQGW%2FB8Gmq0Y51lYOxWcuIxRBoEGZxFTPUFpWbNxv9RtNF6xVQRn8rSYeq65Q%2FFJkOXLesE25u2ooyLdhw3zCaGWHrtXPO5f9ObatQ3I6Sklec36iUTyizi90EktsYSnq8sdi4vCv0eQc%2F2%2FC%2BPDy551O292Gjpqw6IODdgVEtQHlyRYFBmklshk%2FpxEKsOUjOO1WFhPjQETufX3lJWDmHn9BetmwikZ%2FVbEm%2B83SlvmpAqk2mvBYubkIZLNDD3koDQBjqkAfvwVdgYY%2Bwa%2FLHwdUCU%2F6oYlUzZ5JJIBvmPimSvPL0dwHGYrMkknU4Ei5puNFvjqIdA1V5SQkx0Ynl7%2Boi1ZSH4YucwQKEE3pMrP1sDU70TTgqP%2FsCD%2FxHL9HwR%2FOwmHoPjwrx49mkn%2FeRzv3TXHQ0dhrcdztIWuHdZ1hmtGFK9x%2B8CohbdRYaDUC9lEj%2B2uePdV%2FmXGC3IMtBkEM1HUbDehroJ&X-Amz-Signature=4b8b637869c35cd5e086370469aa5967bed2b03ff1a6b7336ff0359233319743&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








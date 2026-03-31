



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYP6I6YG%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T185506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIF3X1a7zwOuL2PipfRsu3ntRClQE1agbSoD%2FBoxgCYnhAiEA5iOf8kmzU2vCceSXhCXf0Xu5%2FfrtpddEoPW4HfNXmhEq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDEsMwNBL5mEb8uGKzyrcA3Na2tBkyW%2B%2FvOwZjXsv%2Bb%2FexhVVAnoamOJkj77da2Dis%2FN%2B%2Bv79ggEfg8U0tCKeKb1llVxKwTOJPzQUDtndz1XYcAwwTBxXrdvNmZRVRfXeX5X7yxEKXSMzaV3kCGaVYfVQ7JHSX4bzZC3EFJWN4R5L2oskKz7AvG%2Bs8mYcsMGrJWaH93ulw%2FNFBTcp9fhMJnM0s6n8qyXv9YVI%2BIH8Zc3awqC8DSrNJ8JuzE4WF1x%2BHVT9bHMEkLsXJCuTGSfQb9ZlwpN5KiOzBX94ajLHDPsbbOt1I2KNjM0WtYqpCx57YcZEZ04IRqdLRvW3534HPPz8o%2FgHP8FYcbtkyTSOw7ncMyoYO3ERO4KJoYIY2qgFmZHAIiqbLPVR3Ca9hey%2BcFTJQQy6zgK8nzsgrbw7e%2FgQqnClAyaQ5sGrMkW43cXzSJ8bwhbQ40Q1Xp%2FNaB8U%2FPQhvhwSv9%2BHBeSAuFaqYoaeOrEqTUFXMjA0pC0oxsShq5zniNPgqP09GpNKLJ5KWQn2q3xEibWjr9hasHvinH78UrXbjPo59s9HMXpO8pz40xZOXMVUMm%2Fbjhh35P6LibjMi0Zp%2FPXmg7rMgfmCn4%2BGozDLTkbkbahEW0Tq8ARsiCcy272QJOHoDn1yMIemsM4GOqUBG%2FJfRKsWOVC5bYElIJs4D%2FUCWadOfkKlKG7MQfS6cJMK%2FCUTllNng0xaoseu%2BCg6Mi10PCY3zMdaW0r%2Fs%2BeBEPgM9u788nGuVSrZ%2FEvg6KCjpCSOodMFSracQqSrlSWARKpu%2FgHBvtE1YQnuyVl76ww6AAyOEl48A1s6G6EN9JrwauzE7kH2MeGozQXzGbaySnviS%2Bb9jETqnYHMYiExTDy2EofQ&X-Amz-Signature=f8920fbb373d536ad38c348aaf9eb0628e26dc4c67020c145ac62c491b1ea5d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYP6I6YG%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T185506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIF3X1a7zwOuL2PipfRsu3ntRClQE1agbSoD%2FBoxgCYnhAiEA5iOf8kmzU2vCceSXhCXf0Xu5%2FfrtpddEoPW4HfNXmhEq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDEsMwNBL5mEb8uGKzyrcA3Na2tBkyW%2B%2FvOwZjXsv%2Bb%2FexhVVAnoamOJkj77da2Dis%2FN%2B%2Bv79ggEfg8U0tCKeKb1llVxKwTOJPzQUDtndz1XYcAwwTBxXrdvNmZRVRfXeX5X7yxEKXSMzaV3kCGaVYfVQ7JHSX4bzZC3EFJWN4R5L2oskKz7AvG%2Bs8mYcsMGrJWaH93ulw%2FNFBTcp9fhMJnM0s6n8qyXv9YVI%2BIH8Zc3awqC8DSrNJ8JuzE4WF1x%2BHVT9bHMEkLsXJCuTGSfQb9ZlwpN5KiOzBX94ajLHDPsbbOt1I2KNjM0WtYqpCx57YcZEZ04IRqdLRvW3534HPPz8o%2FgHP8FYcbtkyTSOw7ncMyoYO3ERO4KJoYIY2qgFmZHAIiqbLPVR3Ca9hey%2BcFTJQQy6zgK8nzsgrbw7e%2FgQqnClAyaQ5sGrMkW43cXzSJ8bwhbQ40Q1Xp%2FNaB8U%2FPQhvhwSv9%2BHBeSAuFaqYoaeOrEqTUFXMjA0pC0oxsShq5zniNPgqP09GpNKLJ5KWQn2q3xEibWjr9hasHvinH78UrXbjPo59s9HMXpO8pz40xZOXMVUMm%2Fbjhh35P6LibjMi0Zp%2FPXmg7rMgfmCn4%2BGozDLTkbkbahEW0Tq8ARsiCcy272QJOHoDn1yMIemsM4GOqUBG%2FJfRKsWOVC5bYElIJs4D%2FUCWadOfkKlKG7MQfS6cJMK%2FCUTllNng0xaoseu%2BCg6Mi10PCY3zMdaW0r%2Fs%2BeBEPgM9u788nGuVSrZ%2FEvg6KCjpCSOodMFSracQqSrlSWARKpu%2FgHBvtE1YQnuyVl76ww6AAyOEl48A1s6G6EN9JrwauzE7kH2MeGozQXzGbaySnviS%2Bb9jETqnYHMYiExTDy2EofQ&X-Amz-Signature=38b02ea058203a727cdc626cc9c1419ea4dd71bb3e803ed9ed7656e55b0647ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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












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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWL52SNA%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T033210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1FiEXNQK74Zd15Rl0uSpwNQPJdRCDRfGPbArYc%2FDOuQIhANGr3ONKb7UzWG7ymMb46cD7nY%2FXLfUeGPzW3UbVmzA8Kv8DCEwQABoMNjM3NDIzMTgzODA1IgzFbFFhFGv%2BPfZ9YZQq3AO1Z29mMgjMqGIxvQN59lZ%2Fv1MIWUY%2FF3dUGYISXI6%2BzD4EO%2FC46snPJgTyz%2BjeUhNcgtQkI2RQVoKmN%2Bn1CG93LBb4%2BP7SqwfwtzIl7WvI%2BzxttPgmyCM3LNWfyAzN9pWXZNjgaBatipd2QtpGkbnjAkrX4WHyFXwTyfzcSKs7mk%2BxOfCqPYOEoTfn3Dh7P7151fnvvd450S%2BJWJ5taHmdImqaYSWIIGTQD%2BmF4iVsRkedwYxDs%2FKkRkQZkBVBsbcWzmNOKwKvnbtrfUu%2B8y0OJXvdK%2FzsnYCzy25Gak8cUhCt%2F1qMOKtRCrRoew%2FQ%2BlhtpJJm%2FuYSzqFnO8IsLtkhXczJS5wWq5P9lGxhjFUi5B96qVKW%2BhJkGUk6%2BxPm3vtv584fWAykcaEtmlmyOhv9kURhOmbliJA%2BCrouM0qF77CGqZAllBA5n%2FYGu2vG2JCRf3sPZmZLzQB6HZMNqZpCRWBopAHpkcBvjZ3kF7PnbfeKFS%2BLxzOcSPw1ws%2BtXPxOLbzDS8u2T442wfZMjdLqmc6v%2BWieNRF0bIQuQvNQtsCPm4NOGUCVwqFBJWAOtC%2BxL1RrCqo%2Fc1qY926%2Bwlm16M5GU01eCTGhIzOufhyddrAqZ43VnRTFRCFi2TCk2YPRBjqkAUzhos%2FlxO6Z797Opw7Ui3y2Orgpa76Q7qota4VEx1XhmDCQ%2BaJ9C7%2F25W0EoLsLc6CvkTVEaCd2n%2F%2BizTo56YctmYVBc%2B%2Bomb%2F7scw5hc1EnB%2B%2FZoHzOHlm2dCje%2F3nLknIdAplfPV9sJK30o6vznm%2BCZ%2Fg7NsuRM9EnByDfelWSSiGw0vHTs%2BI9cFJWdSF9YufeheTB3W1pOX1Tui351NbLQsF&X-Amz-Signature=1e0f330f0fc910c821f9bcaa9da481cb425fef4bf862ea9ee4e70a7ff30e948d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWL52SNA%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T033211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1FiEXNQK74Zd15Rl0uSpwNQPJdRCDRfGPbArYc%2FDOuQIhANGr3ONKb7UzWG7ymMb46cD7nY%2FXLfUeGPzW3UbVmzA8Kv8DCEwQABoMNjM3NDIzMTgzODA1IgzFbFFhFGv%2BPfZ9YZQq3AO1Z29mMgjMqGIxvQN59lZ%2Fv1MIWUY%2FF3dUGYISXI6%2BzD4EO%2FC46snPJgTyz%2BjeUhNcgtQkI2RQVoKmN%2Bn1CG93LBb4%2BP7SqwfwtzIl7WvI%2BzxttPgmyCM3LNWfyAzN9pWXZNjgaBatipd2QtpGkbnjAkrX4WHyFXwTyfzcSKs7mk%2BxOfCqPYOEoTfn3Dh7P7151fnvvd450S%2BJWJ5taHmdImqaYSWIIGTQD%2BmF4iVsRkedwYxDs%2FKkRkQZkBVBsbcWzmNOKwKvnbtrfUu%2B8y0OJXvdK%2FzsnYCzy25Gak8cUhCt%2F1qMOKtRCrRoew%2FQ%2BlhtpJJm%2FuYSzqFnO8IsLtkhXczJS5wWq5P9lGxhjFUi5B96qVKW%2BhJkGUk6%2BxPm3vtv584fWAykcaEtmlmyOhv9kURhOmbliJA%2BCrouM0qF77CGqZAllBA5n%2FYGu2vG2JCRf3sPZmZLzQB6HZMNqZpCRWBopAHpkcBvjZ3kF7PnbfeKFS%2BLxzOcSPw1ws%2BtXPxOLbzDS8u2T442wfZMjdLqmc6v%2BWieNRF0bIQuQvNQtsCPm4NOGUCVwqFBJWAOtC%2BxL1RrCqo%2Fc1qY926%2Bwlm16M5GU01eCTGhIzOufhyddrAqZ43VnRTFRCFi2TCk2YPRBjqkAUzhos%2FlxO6Z797Opw7Ui3y2Orgpa76Q7qota4VEx1XhmDCQ%2BaJ9C7%2F25W0EoLsLc6CvkTVEaCd2n%2F%2BizTo56YctmYVBc%2B%2Bomb%2F7scw5hc1EnB%2B%2FZoHzOHlm2dCje%2F3nLknIdAplfPV9sJK30o6vznm%2BCZ%2Fg7NsuRM9EnByDfelWSSiGw0vHTs%2BI9cFJWdSF9YufeheTB3W1pOX1Tui351NbLQsF&X-Amz-Signature=da954b0e51843cf4b7bf928b82ac0deb5f2fded1cd3792b59f661161fa2a346d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








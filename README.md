



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B3TO7XH%2F20261020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261020T001949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQCJjD%2F3C2fu5KXvkmqXTNLDN8ldXmMNvUL0tgY%2F6abjVQIgQDkr7F7PiawalB1Q1X%2BEiuDq95fkUCqJeulqlfPQxbAq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDMpgpEhulNz9HcxO0yrcAxiiWgI7msR47O60yYwThJXrdpzngACpFoyZ2I0aJvegrZEtsibcFZGwFOMazMHwWPQdq9V4XhQHD1lBlTU1aR53ILWXf7xQgDTYIK2TXwNGdrhwlpYkiVOedtu52p5Pxz%2FSf9Z3Bsi0rYR%2B52ENB3Nb%2B92YfWKiMK04HzlqgziAxIkUus2FASoj4pvcLz%2BU7c1AxZ6IZKl5twQ2u1KBTjlZi3HxvT8z9y4aV27uGyLuGGK7sdh%2B4G%2BOghEV1qEbJuwziZfw0tuAyMsg24CybPKJom1RRqFF5cU%2Fc1zNLdppbRnFub7spifSrFSTJ9b1PjfblqPWuM5DLYH7%2B%2FKZHokM2UwOvjDtUQTb9Majf6Jha3%2FJ4RUCqvoACmHyWQGKcUKa5IPG%2FzHAf7t4FgjacfZvmyUog5JUCZL8K9qBS7IdqGvR17cqF2bNt8GkMugs5b4kVLUDzyb0I%2BgXMmw1vj1v9R6GHAguUiRyYbmVyHLcUc4%2FT%2Bl4rSA7U3T5DHdC228YmlcVVXnp41J0Ek86JvgO61kPDIfSirlih4LGwZE05aquyoMGIQxd9nXrZkJvVnb%2FRTZU6L9M1AvqOXkhMo%2B4XoVyhS1RPH121EW7XZQXPp%2B%2FPLRVwsLTDKjyMP%2FE2tYGOqUB30PmupQN%2FGRZuzEw8903rWs4zzomRXZBHeFUNXzp3mTLm4PS6P3wEEVJ95vWD0qj0H4mY3ZxOivmTUQ3l1GyA3QKf4b9o5EYmsTMx%2FcsDv2T4SHPDFHU0kG4VKsv0Q1rqloFrSxAP4SPd%2BhBBJi9QsFXzRGb2OJhczvydMyvP1u3T9FpsLKYGj%2F6wghepAzsV2fLE4g5sBmmyDJTuZLXQLVyf1lb&X-Amz-Signature=ee00a2d905a96a63ff0582adf2ada5a343fdf32611ca6ccc247abc6322cebba6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B3TO7XH%2F20261020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261020T001949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQCJjD%2F3C2fu5KXvkmqXTNLDN8ldXmMNvUL0tgY%2F6abjVQIgQDkr7F7PiawalB1Q1X%2BEiuDq95fkUCqJeulqlfPQxbAq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDMpgpEhulNz9HcxO0yrcAxiiWgI7msR47O60yYwThJXrdpzngACpFoyZ2I0aJvegrZEtsibcFZGwFOMazMHwWPQdq9V4XhQHD1lBlTU1aR53ILWXf7xQgDTYIK2TXwNGdrhwlpYkiVOedtu52p5Pxz%2FSf9Z3Bsi0rYR%2B52ENB3Nb%2B92YfWKiMK04HzlqgziAxIkUus2FASoj4pvcLz%2BU7c1AxZ6IZKl5twQ2u1KBTjlZi3HxvT8z9y4aV27uGyLuGGK7sdh%2B4G%2BOghEV1qEbJuwziZfw0tuAyMsg24CybPKJom1RRqFF5cU%2Fc1zNLdppbRnFub7spifSrFSTJ9b1PjfblqPWuM5DLYH7%2B%2FKZHokM2UwOvjDtUQTb9Majf6Jha3%2FJ4RUCqvoACmHyWQGKcUKa5IPG%2FzHAf7t4FgjacfZvmyUog5JUCZL8K9qBS7IdqGvR17cqF2bNt8GkMugs5b4kVLUDzyb0I%2BgXMmw1vj1v9R6GHAguUiRyYbmVyHLcUc4%2FT%2Bl4rSA7U3T5DHdC228YmlcVVXnp41J0Ek86JvgO61kPDIfSirlih4LGwZE05aquyoMGIQxd9nXrZkJvVnb%2FRTZU6L9M1AvqOXkhMo%2B4XoVyhS1RPH121EW7XZQXPp%2B%2FPLRVwsLTDKjyMP%2FE2tYGOqUB30PmupQN%2FGRZuzEw8903rWs4zzomRXZBHeFUNXzp3mTLm4PS6P3wEEVJ95vWD0qj0H4mY3ZxOivmTUQ3l1GyA3QKf4b9o5EYmsTMx%2FcsDv2T4SHPDFHU0kG4VKsv0Q1rqloFrSxAP4SPd%2BhBBJi9QsFXzRGb2OJhczvydMyvP1u3T9FpsLKYGj%2F6wghepAzsV2fLE4g5sBmmyDJTuZLXQLVyf1lb&X-Amz-Signature=9cf5d1347743029848a223f68b04ba92c5920631f3baff29063be95e37bbe73e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








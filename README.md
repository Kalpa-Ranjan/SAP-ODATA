



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643QSTYVL%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T014226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIA1g09LT0NuCZTJCsN9gxv3GfRjCn%2BI%2FUovuCKT%2BmW2dAiAgxyjZAFpGD%2F%2FMOSXBPU9pVBYbQr4ji%2FUWM4%2FRlytGYyr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM19ngraJ2SVO6L6eJKtwD97MZzb%2Fs91p0ym%2F90rKXN48Y5h9ZtPTMp284PbIPiYf4XuNO4VGu7yARz0MeOpuHLHvxpCP9PQsvxpHsMHOm54y95LdcJRGpte447yaA1%2Fbt3CYLQ%2BuY1Mv1jo6yrryzWBJ1mb87pD1%2FZIxUJEc8H2RGcrZA%2Bn2ZnEgG3gKmrw3w7UetDwAuhT1pStErn7BQVzXfIzonZH%2BjE0bhbdRNOg7NELDCWnC21QkFQbQDSmNuwSQFwej7pbeFWGxIxMFzooucuwnyVarLr8hMGlLDNgo6yjbLsYqrdW%2FxC2mvMYyk%2BwGDca6QbBvgBPEZFzzR%2BWIjuzVKSPW78izMuVMxTnGk9WbAiEbTBpS%2FrHXA1RzKo%2Ftzm1%2BZMdFTieZVsZTKeVXoGX0WSTyLmCjSBT1TMBMiRWp22UZ0K%2FLMJxGYN2FmfsZSACT4IumlHb%2Fs%2FNtOFrDYQMIJVhKaRo1f1mDArUDLUjO5Sug5lDB3ZM0W4hHWQzhiO24mM6gOnDJKNOPCtBdnFWaRoxpJIKAqM%2FTsp5bTmftx8KjGbKgfH5uLersMNSXyiqTC7WfJiifxRebKVZCnHO%2FSxMrd1PnflNH5HNorpmOnsGG%2B56ft%2Fs2Dp6dwJMajde31nvWagcYwutmDzQY6pgGAlC0aCClhmFqMM6OwZnizOGge9TGfofiGKaUIHRwj8sH%2F7NBq5eS%2BHP7foUazocYck%2FR4EPtzRjAEamyM%2BLjT2vRzAEMyeJwzY4FwSAaaosGU%2FJpiLg60GqYriINJsJGZYyObVr82wXTnHVuGlkHD%2FIS2gQJoBGDd51feBPtz2j46sE2b3eiW2HShn71lcbE6DMfKkUVtrbJV3W9gjt%2BdEwiggQnB&X-Amz-Signature=c001e9e9b3d1326344d1da1b925d95d63f8cc0445ea988014de01e0684527788&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643QSTYVL%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T014226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIA1g09LT0NuCZTJCsN9gxv3GfRjCn%2BI%2FUovuCKT%2BmW2dAiAgxyjZAFpGD%2F%2FMOSXBPU9pVBYbQr4ji%2FUWM4%2FRlytGYyr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM19ngraJ2SVO6L6eJKtwD97MZzb%2Fs91p0ym%2F90rKXN48Y5h9ZtPTMp284PbIPiYf4XuNO4VGu7yARz0MeOpuHLHvxpCP9PQsvxpHsMHOm54y95LdcJRGpte447yaA1%2Fbt3CYLQ%2BuY1Mv1jo6yrryzWBJ1mb87pD1%2FZIxUJEc8H2RGcrZA%2Bn2ZnEgG3gKmrw3w7UetDwAuhT1pStErn7BQVzXfIzonZH%2BjE0bhbdRNOg7NELDCWnC21QkFQbQDSmNuwSQFwej7pbeFWGxIxMFzooucuwnyVarLr8hMGlLDNgo6yjbLsYqrdW%2FxC2mvMYyk%2BwGDca6QbBvgBPEZFzzR%2BWIjuzVKSPW78izMuVMxTnGk9WbAiEbTBpS%2FrHXA1RzKo%2Ftzm1%2BZMdFTieZVsZTKeVXoGX0WSTyLmCjSBT1TMBMiRWp22UZ0K%2FLMJxGYN2FmfsZSACT4IumlHb%2Fs%2FNtOFrDYQMIJVhKaRo1f1mDArUDLUjO5Sug5lDB3ZM0W4hHWQzhiO24mM6gOnDJKNOPCtBdnFWaRoxpJIKAqM%2FTsp5bTmftx8KjGbKgfH5uLersMNSXyiqTC7WfJiifxRebKVZCnHO%2FSxMrd1PnflNH5HNorpmOnsGG%2B56ft%2Fs2Dp6dwJMajde31nvWagcYwutmDzQY6pgGAlC0aCClhmFqMM6OwZnizOGge9TGfofiGKaUIHRwj8sH%2F7NBq5eS%2BHP7foUazocYck%2FR4EPtzRjAEamyM%2BLjT2vRzAEMyeJwzY4FwSAaaosGU%2FJpiLg60GqYriINJsJGZYyObVr82wXTnHVuGlkHD%2FIS2gQJoBGDd51feBPtz2j46sE2b3eiW2HShn71lcbE6DMfKkUVtrbJV3W9gjt%2BdEwiggQnB&X-Amz-Signature=8bca14dbab4766d098c95f3e90df34713f0d9200f589e14fd8c368c64940f358&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








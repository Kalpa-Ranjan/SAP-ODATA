



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2NL56QX%2F20260504%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260504T192146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk0GBzoqx0Nf9cSk8tvzuFqwt73i7YeMWOSpUlgw4stQIgUcePCAdd7mEQicbxKW2ELUsRZkXTMviUg2dm590jQqUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMknDlygiALN9f8NCyrcAw0uZFvS94pMFAcBt6ZGRSVgKGf4GmwuM9%2B4aR%2FMzjQ%2BMi3dHH2tgoGPk6qZzdT9yGH6%2FXj2dex08yeGlqxxgRQ6FBVEmJ%2BOjEGV51rqqfzQFXToXhBK1wLrzHB4i2V0xiAPwCGg3mpuxEiGlXPtLtozVqFW5nEiIOhN3Sbn61q7g4g%2B62IwMsGywq0SbYpRhIvJJS5pN6mjyxK7wSMe1KGT7a4CSasqeUqz4KQ%2F%2BROIg6lVPttITV5entSCt9LkmcaZb8gZlcv4r18ciMFA%2BpZJyw6wg99olchdQwbPNjs8%2Brm9XxI6BRaU8uHghQulp1m%2B6yFojL6pEYa7XNRY3GF4Xdo6KWsi7M7pvhPqLytVKm215J%2BcDowjmbrdudVgWxBz3f8dUQTZIvF%2FFiHWPtXbzrDQTA6gRVCO%2BFwIVXi2RtOTpW6ZRAAJpZQiGqcaple1Mwm16pzZ2psizU%2BrhkfXYd6vWJa6XvlmzZVtZ55Woo5PpRjLpbJ02cJhXyPEQfNZqOiKoKWubl0Ick94ioYahbNG4b04UvSQfNJqw7PWmqkTkzoy8nlPCo1kmDrQjBYXxP%2FawtUxtI1XKuPRcS5xTj0DvCRyJOCW444fvjiRSMAMypxooHBDUCuPMLrN488GOqUBjgqJ%2BmyvZDuoR%2FOyNSYAFLRq3d%2FAtrP3dePxcDgetAqhPZCpRlwnDBOARnHPRymgDG7OmT35RvBENJcW7yjm9NI%2FzGIE%2BVP90E9gqNLGSfdxGSOXgoDvPfMT%2FmPOUw0dBLTa16S6wm1hhqW4rq8ZvZD2iCOEr50o5JLIah%2BQ2CyTGV3VaqPJN%2B4dEir8MnbKKJb1en7fK7q7%2FT4lMql05LyZJ6Vt&X-Amz-Signature=dadc1f6022f5685cee390fc1d9aa832231522f011c2c700274e48fb2ae496273&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2NL56QX%2F20260504%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260504T192146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk0GBzoqx0Nf9cSk8tvzuFqwt73i7YeMWOSpUlgw4stQIgUcePCAdd7mEQicbxKW2ELUsRZkXTMviUg2dm590jQqUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMknDlygiALN9f8NCyrcAw0uZFvS94pMFAcBt6ZGRSVgKGf4GmwuM9%2B4aR%2FMzjQ%2BMi3dHH2tgoGPk6qZzdT9yGH6%2FXj2dex08yeGlqxxgRQ6FBVEmJ%2BOjEGV51rqqfzQFXToXhBK1wLrzHB4i2V0xiAPwCGg3mpuxEiGlXPtLtozVqFW5nEiIOhN3Sbn61q7g4g%2B62IwMsGywq0SbYpRhIvJJS5pN6mjyxK7wSMe1KGT7a4CSasqeUqz4KQ%2F%2BROIg6lVPttITV5entSCt9LkmcaZb8gZlcv4r18ciMFA%2BpZJyw6wg99olchdQwbPNjs8%2Brm9XxI6BRaU8uHghQulp1m%2B6yFojL6pEYa7XNRY3GF4Xdo6KWsi7M7pvhPqLytVKm215J%2BcDowjmbrdudVgWxBz3f8dUQTZIvF%2FFiHWPtXbzrDQTA6gRVCO%2BFwIVXi2RtOTpW6ZRAAJpZQiGqcaple1Mwm16pzZ2psizU%2BrhkfXYd6vWJa6XvlmzZVtZ55Woo5PpRjLpbJ02cJhXyPEQfNZqOiKoKWubl0Ick94ioYahbNG4b04UvSQfNJqw7PWmqkTkzoy8nlPCo1kmDrQjBYXxP%2FawtUxtI1XKuPRcS5xTj0DvCRyJOCW444fvjiRSMAMypxooHBDUCuPMLrN488GOqUBjgqJ%2BmyvZDuoR%2FOyNSYAFLRq3d%2FAtrP3dePxcDgetAqhPZCpRlwnDBOARnHPRymgDG7OmT35RvBENJcW7yjm9NI%2FzGIE%2BVP90E9gqNLGSfdxGSOXgoDvPfMT%2FmPOUw0dBLTa16S6wm1hhqW4rq8ZvZD2iCOEr50o5JLIah%2BQ2CyTGV3VaqPJN%2B4dEir8MnbKKJb1en7fK7q7%2FT4lMql05LyZJ6Vt&X-Amz-Signature=ce516f34bc43916afaff0eb96ffe6df0530cab117e36108fab8e5371ce35fe06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








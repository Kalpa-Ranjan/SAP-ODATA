



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VT437KL%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T025602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDBOg32qdxvMouD6UVc8ZuM9l289pFBpdIrWxjDXRLzKwIhANEB5FnxBVk7j9lk5rit0eMyyXOOYtCzg%2Bo2rd75e8hNKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxg8IVhS9DK%2B%2Bsq6Fgq3APh0aEhi5S0q8c3LWpM3917E%2BEYCvPJHzGKkzjPtkjnyBkmSkvf4xTvWpmifIG6eZknZJUjnlxELNu5i4B1teY6Po0%2B8PPN5mRyvRFT4Rm6C4rj5zT28o0fsf%2FG4y5RiRmDI6SGFE5Mdtq0niIM8LNvbZmvqfv0%2Fl29O7miJLcdG7ukWutfX%2F7Fdnco5L%2BQzElq47IqX8GU0g4%2FMQp81ruZLNyR0peVs5pV4t3kTHIx%2FyjKSrckw%2Fa5Gfq5bOyPtnjxcwjZToJZIm45e5sth1XpHjXg9padhBx80QxyNmLCCi7YJedP1C1hf4n03gJlcge5klSORR56LT7VBviV0A444g6%2BPhHpRuRMnrVSEAdySQP%2B8cq%2BNyKNxIZHAa08nwMKFxhEKAvQvpg2f7ABfzcM8thmzWVPE0QDPBGSa4dbBQnUb81KyCZTR9ijKMIhYK80Z%2FOVRxN4P0qdoUhNnQErbdhInbVBg5bOjrPAnxcaxpE8L0Ni7EDTHj31HsTGhl8QX6d9D%2BEh1yy7fckSEoFv3GfE%2BWNwG7eKEx%2FZfwzSPKGxRUzlvhJmn5wYIHmTo5rfVGYEHHye7Df17ZE4u6ExVUzNKVdjqATM7Ls%2F%2Fi9BXDFeTk6cSjEWAzOlHzCP55DSBjqkAafxK9PIxnRfJgniOi8UaK%2FJJX1h5ZCTBSA3LqcKs%2Bjr1Wd9XRD47sodk9lwwwX6x5sbPZ7f005I3UxOHHSz8baXZvsHOdt1gv%2Bp%2F09gWse2bcq8OPOc%2BK8bRLPyVV0dB11tDcg41PXruXMYRmRze86hsRBNU6EpiqvzOowul4jMp2qjWO0ROBhbp17exGT58ZKQT7%2FGJjxqEqSfJH7C7ZPh%2FDCd&X-Amz-Signature=f7f7e134fb50ec4a4852b6467e003860ed371f68148e153fd363682ace37f4ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VT437KL%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T025602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDBOg32qdxvMouD6UVc8ZuM9l289pFBpdIrWxjDXRLzKwIhANEB5FnxBVk7j9lk5rit0eMyyXOOYtCzg%2Bo2rd75e8hNKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxg8IVhS9DK%2B%2Bsq6Fgq3APh0aEhi5S0q8c3LWpM3917E%2BEYCvPJHzGKkzjPtkjnyBkmSkvf4xTvWpmifIG6eZknZJUjnlxELNu5i4B1teY6Po0%2B8PPN5mRyvRFT4Rm6C4rj5zT28o0fsf%2FG4y5RiRmDI6SGFE5Mdtq0niIM8LNvbZmvqfv0%2Fl29O7miJLcdG7ukWutfX%2F7Fdnco5L%2BQzElq47IqX8GU0g4%2FMQp81ruZLNyR0peVs5pV4t3kTHIx%2FyjKSrckw%2Fa5Gfq5bOyPtnjxcwjZToJZIm45e5sth1XpHjXg9padhBx80QxyNmLCCi7YJedP1C1hf4n03gJlcge5klSORR56LT7VBviV0A444g6%2BPhHpRuRMnrVSEAdySQP%2B8cq%2BNyKNxIZHAa08nwMKFxhEKAvQvpg2f7ABfzcM8thmzWVPE0QDPBGSa4dbBQnUb81KyCZTR9ijKMIhYK80Z%2FOVRxN4P0qdoUhNnQErbdhInbVBg5bOjrPAnxcaxpE8L0Ni7EDTHj31HsTGhl8QX6d9D%2BEh1yy7fckSEoFv3GfE%2BWNwG7eKEx%2FZfwzSPKGxRUzlvhJmn5wYIHmTo5rfVGYEHHye7Df17ZE4u6ExVUzNKVdjqATM7Ls%2F%2Fi9BXDFeTk6cSjEWAzOlHzCP55DSBjqkAafxK9PIxnRfJgniOi8UaK%2FJJX1h5ZCTBSA3LqcKs%2Bjr1Wd9XRD47sodk9lwwwX6x5sbPZ7f005I3UxOHHSz8baXZvsHOdt1gv%2Bp%2F09gWse2bcq8OPOc%2BK8bRLPyVV0dB11tDcg41PXruXMYRmRze86hsRBNU6EpiqvzOowul4jMp2qjWO0ROBhbp17exGT58ZKQT7%2FGJjxqEqSfJH7C7ZPh%2FDCd&X-Amz-Signature=ce6d190d1907db9e2acd70e005baab4f990f87ff9b75954108b57b8044e5798a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








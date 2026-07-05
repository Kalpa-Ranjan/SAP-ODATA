



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUFKQDCZ%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T023618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIBtZpum5CTtuc5MoaYAg1WgFQZMmOR5y7jpfh%2Fbj7bKLAiB9dNU46royUjrWx2FWRLsLiXSvVO0MYeSQRQVGUSKR%2BSr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM%2FgNqpXIV92MtmzzwKtwDbEbzavXpjKXmlD901%2FVR5OSkx7DRKVfVFZzIzir6M7w9wCv8kp77OlW5ZW7bToJvJK0W78XyKxVrYhfJMw1utFuzqdJs%2BxFuyspuDOO5Xo1XnhklJQPKueFuu8VkRPSnXszA6k%2BKdwbef8kbjn0PnLoKgZyxVskw%2Bj05Y7q6RmLdmsGpRIRP2hxOMqjcBk4Z%2FbvJ%2B8SB3iJ%2FHPicSd8hcW9y%2Fcbr5L12Vi1X4crz66K2Z6Udf0LtfFMRt5%2BUlT1kKYzFzD07EV2ONquqKC6No2VFAXJRGe2ovyqH6xBOgyWU%2BwIA%2FuZhRtrDahdCHc9er0cgijhM4ElZh5RgHHp1%2FVr5HIOP3eCBAWyNxGa6B17ICYqMcLMHcucDgm09j40Tbie3jJC8IbP6DKnVyM6Be8zpQanobJzuguL5HrFE5DHYReEgdjTkuhPJhNX7rTvjhd%2FetZ6oiVYylxSKWLdnyWxICOczYA5tEmTpmyqAPMAdDaPjEW0w%2BPRyRvn9qRS8Mz0XtN1fEPGaJGxvu1uWVB9CR%2BoaAaZWykgIaswEi1LT4lOUKHtaIKI3Mi6rYsOAvN09MTj7WYqy3z2mylxkk6VVNUINLW%2B%2BXwkk2F5ybvygUgOn7fC4sp05SFIwmNum0gY6pgGVesVPuhixB2WePx3zobOOztoDN1Pfepwf6pFCIZbyiRavqxI2U8CxtlFoBMBs0bGAif6u9OnfWPt%2BC55qca400sf81Crav%2BqFUD2nPFJ2iIEUt810j3QlqOm9rHFfMIzW2AP6l3RkzZXfWNrUmS5xj%2BnEFqGOre6wcHYczK927hzd8FEChc41GjDoL8rKke9muU7MSn8cRs%2F9%2FHcYdyTzJ7mZxJoz&X-Amz-Signature=120b549e8fa519480b0358250203aa3f6d895a742a2ee9c2fd5fe52f3b6e8a1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUFKQDCZ%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T023618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIBtZpum5CTtuc5MoaYAg1WgFQZMmOR5y7jpfh%2Fbj7bKLAiB9dNU46royUjrWx2FWRLsLiXSvVO0MYeSQRQVGUSKR%2BSr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM%2FgNqpXIV92MtmzzwKtwDbEbzavXpjKXmlD901%2FVR5OSkx7DRKVfVFZzIzir6M7w9wCv8kp77OlW5ZW7bToJvJK0W78XyKxVrYhfJMw1utFuzqdJs%2BxFuyspuDOO5Xo1XnhklJQPKueFuu8VkRPSnXszA6k%2BKdwbef8kbjn0PnLoKgZyxVskw%2Bj05Y7q6RmLdmsGpRIRP2hxOMqjcBk4Z%2FbvJ%2B8SB3iJ%2FHPicSd8hcW9y%2Fcbr5L12Vi1X4crz66K2Z6Udf0LtfFMRt5%2BUlT1kKYzFzD07EV2ONquqKC6No2VFAXJRGe2ovyqH6xBOgyWU%2BwIA%2FuZhRtrDahdCHc9er0cgijhM4ElZh5RgHHp1%2FVr5HIOP3eCBAWyNxGa6B17ICYqMcLMHcucDgm09j40Tbie3jJC8IbP6DKnVyM6Be8zpQanobJzuguL5HrFE5DHYReEgdjTkuhPJhNX7rTvjhd%2FetZ6oiVYylxSKWLdnyWxICOczYA5tEmTpmyqAPMAdDaPjEW0w%2BPRyRvn9qRS8Mz0XtN1fEPGaJGxvu1uWVB9CR%2BoaAaZWykgIaswEi1LT4lOUKHtaIKI3Mi6rYsOAvN09MTj7WYqy3z2mylxkk6VVNUINLW%2B%2BXwkk2F5ybvygUgOn7fC4sp05SFIwmNum0gY6pgGVesVPuhixB2WePx3zobOOztoDN1Pfepwf6pFCIZbyiRavqxI2U8CxtlFoBMBs0bGAif6u9OnfWPt%2BC55qca400sf81Crav%2BqFUD2nPFJ2iIEUt810j3QlqOm9rHFfMIzW2AP6l3RkzZXfWNrUmS5xj%2BnEFqGOre6wcHYczK927hzd8FEChc41GjDoL8rKke9muU7MSn8cRs%2F9%2FHcYdyTzJ7mZxJoz&X-Amz-Signature=bc62bf973e63ba6533d67aab3285ee905ab336734e0aa6317f5fbea32568c3be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








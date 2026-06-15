



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N3GQGH4%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T204952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHIibRQflu%2B1pTCoWllHfPpv%2FYWlHiQzmJi7gTjuv38AiEA4pbvjGhqctfNuzqY0qFmqfI28cfQTM6eRJQ%2F6lBwufYq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDBrPe4m5si7xdkP3WSrcAwl7IabP44fKLc2OaKV5SXgjM%2Byp38IK8Y3Tn%2BGzCE7ilC55K6FQMkXt3jwdx1FuseHlpQ9slqrkUnGzvNIj%2BsguxopvfPmz4HfLNLNlg4eYjA0yJBwOvJV4XJ951kCVemTOePutkEw7BqzLS65KZdNQstvx2zguDHlw7EZlFM8M4qfGMVZPzzFKTSykR%2B%2F4LMc%2FO0MQhURHz1aes09MbpsjWULCjprPE%2Bq3U4dQ2YmyrlhaHtvBe7zo2OzGFsSZqcmVqFC98DAPlNH3JRy86BGZMfx1TREtPfqKmHeRKz7g6fAK7ik7ADpcFboiQWGYFsgWPRGijdR1HpPEhLHbLEdyB%2BL60ViCAa0xvE3xxOhbbRrB7jamoLx5F5TksGPin8HLnMGyiB6LJ2tsFDo7nM2lHGiwPSw%2F8zSJLrHRQqpvYTXSzHgxSRtCXESpeCfBi006kaB4%2BfkzCauZcB2qcbJlp9cAYTIASc8dX3yDeFpGAAYs3ya%2BqOlF2OPDY9b%2BfaYf5Ekl10Q2ZVqDrGWtD9%2BIsxJqO%2FNXCbYhDtPxNOsfWGiOJakL2vQDHTmPnH%2BrYevm8%2Fs4qH16YNsmn8IO3nlsu9NO2Wk0Esu2nsg89AqMnAkdba1XlwepB543MMGqwdEGOqUBCZkglG0x9ywdQ2rXKP3rnrJeiOkkHG%2BJS7%2Fo%2BZeCRjYOIFdKDZVRI7OIunl3PopzjNZWFiFj%2BLBOeZDgoaVFKkDlQYHk8p5cRWUvSRUKdzfJpY6tgnVVuQO540Dp0JBl0t5iGb0VNpIUgk5STa2k7igMD%2BPenBFDUTwyK6QSXhTVPRrl3ig7tSjjs%2F1zEY5wPpcux4e06sKGQi6eWCbhHK4Z%2Fw95&X-Amz-Signature=581e6f6863c2bc515335cf97419beffb2a2ddd6d81a56ab3b9d66a0ee0e4411e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N3GQGH4%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T204952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHIibRQflu%2B1pTCoWllHfPpv%2FYWlHiQzmJi7gTjuv38AiEA4pbvjGhqctfNuzqY0qFmqfI28cfQTM6eRJQ%2F6lBwufYq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDBrPe4m5si7xdkP3WSrcAwl7IabP44fKLc2OaKV5SXgjM%2Byp38IK8Y3Tn%2BGzCE7ilC55K6FQMkXt3jwdx1FuseHlpQ9slqrkUnGzvNIj%2BsguxopvfPmz4HfLNLNlg4eYjA0yJBwOvJV4XJ951kCVemTOePutkEw7BqzLS65KZdNQstvx2zguDHlw7EZlFM8M4qfGMVZPzzFKTSykR%2B%2F4LMc%2FO0MQhURHz1aes09MbpsjWULCjprPE%2Bq3U4dQ2YmyrlhaHtvBe7zo2OzGFsSZqcmVqFC98DAPlNH3JRy86BGZMfx1TREtPfqKmHeRKz7g6fAK7ik7ADpcFboiQWGYFsgWPRGijdR1HpPEhLHbLEdyB%2BL60ViCAa0xvE3xxOhbbRrB7jamoLx5F5TksGPin8HLnMGyiB6LJ2tsFDo7nM2lHGiwPSw%2F8zSJLrHRQqpvYTXSzHgxSRtCXESpeCfBi006kaB4%2BfkzCauZcB2qcbJlp9cAYTIASc8dX3yDeFpGAAYs3ya%2BqOlF2OPDY9b%2BfaYf5Ekl10Q2ZVqDrGWtD9%2BIsxJqO%2FNXCbYhDtPxNOsfWGiOJakL2vQDHTmPnH%2BrYevm8%2Fs4qH16YNsmn8IO3nlsu9NO2Wk0Esu2nsg89AqMnAkdba1XlwepB543MMGqwdEGOqUBCZkglG0x9ywdQ2rXKP3rnrJeiOkkHG%2BJS7%2Fo%2BZeCRjYOIFdKDZVRI7OIunl3PopzjNZWFiFj%2BLBOeZDgoaVFKkDlQYHk8p5cRWUvSRUKdzfJpY6tgnVVuQO540Dp0JBl0t5iGb0VNpIUgk5STa2k7igMD%2BPenBFDUTwyK6QSXhTVPRrl3ig7tSjjs%2F1zEY5wPpcux4e06sKGQi6eWCbhHK4Z%2Fw95&X-Amz-Signature=ef36031283ed5aeed1d55977cf98eb26ec032277b15f1f2a07985e56d3449421&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








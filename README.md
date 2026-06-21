



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVZLWLLN%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T192258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCa%2FkhMQLTDbwd3SiR4CxkaIHWAE%2F1j5ynW7VryKx6k2QIhAOPACXNqhxQpmD01axDUJZJ%2F2qFNJ7y1H8o87sY6G7FfKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzwkb5%2F3P29UKP3TnAq3AMQ1Vf8Tt5HoObcdboKFNZ6bzQNSoZrCUYFzK1GGj%2F68Z8udq9rNrvSkhIaTiBoYkNEdPUMBLA3vS7TTjWdW%2FHYx4tP4TsCbN7WjsHrqMXg4mZMUIFFcHMGvghJDZQJyq1j9b%2BxWUUP2n9wYlw88aAmYlYEbsLtTsxI5EtvohDXTtOSHRrZ0SCVz4qG9t%2Fngd662sWMmFTDxVm2Ji8u6P74uoD4Wk5jrBckBf%2BbLdt%2BTghhBFc6GKTgfN02DRilmr01AM6RZAvzaVEjuIP%2B5YWzZebTrt5raGIevwb5ok0UcnpngZXc3xUAjyfijzX56Ya30itIFL77vsT8IHlbtoKeiL19%2BeHWNd6wpJPMgJCKPgNUvaRRhdv6ByQqFgH%2FNHRBgTX2klu73w8wNjj89UsIfUW45sJI5OlcMgGJxjqAmj2LMBCfPCLL4hN5%2BAgSgJhPbe%2BaZZNbx1IbQBJEnoaty9TW6Y80EhRJViiUfRtnAPVY658qjIa4e5XJLpFV39w4tO5jM7q1FXYritpL9Z4b9cIGoetB7ybMlyR87MIUApgRUViaRroy2Ecg324a55erUOb6H3t8ZEDmI%2FYJkigXHoo9T5PG2dpAc7hybsXjxKVUzIs5YnCHYwYRyzDMo%2BDRBjqkAVk2lvaKnXuM%2BhMT7AAO0GlGyFW34QZ9iNLcmZ%2BqST7DB2THUI8ZWBsZAQDjlig7tHgahxA5%2FY7kX0E4WNA066VkZqS1p5M6KVBNvvpsNmQ%2BcxVt1dTkKw3YYhFj9d61%2B%2FoeSMuN%2FfQQNq32plFvgLuatNstYEavwbsPwP5it9nE%2FOgTe0614hIb3Yh1U6uvtKOJh6%2BAZKDABSkfLI3Vbpi9%2FZ4Q&X-Amz-Signature=618702d88da57c0108c65d94dc02af6e077f2651055b41cf073731bb0558d310&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVZLWLLN%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T192258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCa%2FkhMQLTDbwd3SiR4CxkaIHWAE%2F1j5ynW7VryKx6k2QIhAOPACXNqhxQpmD01axDUJZJ%2F2qFNJ7y1H8o87sY6G7FfKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzwkb5%2F3P29UKP3TnAq3AMQ1Vf8Tt5HoObcdboKFNZ6bzQNSoZrCUYFzK1GGj%2F68Z8udq9rNrvSkhIaTiBoYkNEdPUMBLA3vS7TTjWdW%2FHYx4tP4TsCbN7WjsHrqMXg4mZMUIFFcHMGvghJDZQJyq1j9b%2BxWUUP2n9wYlw88aAmYlYEbsLtTsxI5EtvohDXTtOSHRrZ0SCVz4qG9t%2Fngd662sWMmFTDxVm2Ji8u6P74uoD4Wk5jrBckBf%2BbLdt%2BTghhBFc6GKTgfN02DRilmr01AM6RZAvzaVEjuIP%2B5YWzZebTrt5raGIevwb5ok0UcnpngZXc3xUAjyfijzX56Ya30itIFL77vsT8IHlbtoKeiL19%2BeHWNd6wpJPMgJCKPgNUvaRRhdv6ByQqFgH%2FNHRBgTX2klu73w8wNjj89UsIfUW45sJI5OlcMgGJxjqAmj2LMBCfPCLL4hN5%2BAgSgJhPbe%2BaZZNbx1IbQBJEnoaty9TW6Y80EhRJViiUfRtnAPVY658qjIa4e5XJLpFV39w4tO5jM7q1FXYritpL9Z4b9cIGoetB7ybMlyR87MIUApgRUViaRroy2Ecg324a55erUOb6H3t8ZEDmI%2FYJkigXHoo9T5PG2dpAc7hybsXjxKVUzIs5YnCHYwYRyzDMo%2BDRBjqkAVk2lvaKnXuM%2BhMT7AAO0GlGyFW34QZ9iNLcmZ%2BqST7DB2THUI8ZWBsZAQDjlig7tHgahxA5%2FY7kX0E4WNA066VkZqS1p5M6KVBNvvpsNmQ%2BcxVt1dTkKw3YYhFj9d61%2B%2FoeSMuN%2FfQQNq32plFvgLuatNstYEavwbsPwP5it9nE%2FOgTe0614hIb3Yh1U6uvtKOJh6%2BAZKDABSkfLI3Vbpi9%2FZ4Q&X-Amz-Signature=a6ed0a7dec9402b7e009f06d5a3bd131ee694cc85dc554b96ed73b43c277ce6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








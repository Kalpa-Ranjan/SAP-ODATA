



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CC5CRFT%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T123553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGY6NYh253gqlZnUrdne5boX2OE9vYc6UG9L%2B8kX8ZHmAiBJ8zrcxZ4eMoMXD6oyIq5%2BJwNdzDCj0Tsjpwdc0g27hSqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLPzhEfTlPVHDommeKtwDF4liZh%2BzImzOG8Eih7BTdEdLPRFUXjN67UN7%2BUGJ45gd2fT86h%2F0m%2BH%2Bf3M8KAN%2FkaLbR5kPlZ3qyamxz6aZqCx%2B8O5IM9CbQdVVcSXJCtWd48cTYPtI6xEfYuCIPAT5eIYAyQLTjoThUcUrxBoxsCfd3iZlP%2BHupPollzcomPe4qYb2eQihSxUBLrXfLu3njTpqXh%2BGa9dIknrv9wuby7N8im7bKYvglw3S56jjSGkvHzIJ16xs%2FHE8Z%2FpR9asx7fkWR4DyjSprBOMfmmfV%2BOZn0NNQqhxRoW81CmRWHrSnNq3rkFJ5ZX1ODLdTVb5iadHxiUMyjugcn%2F357SeXE%2FbGKI%2FPCNvh5CSV8hd6h7aKGPfivDbhuD8pnqgVuqpKJoMkJXCmaG9w6pSdreJF4gupg12WlvuPmEtyeB%2BARsvRwdkWdRYHWI60LFYTtE3egHGcFBcWWjZ4hXNRnicF%2BMSKLPimQq7t7WKvw1R232nGONcvVn6eVRCatN5pcJNyHWgg4RqUQ4DXxdfzum2fLFUKm47ShT1KFwwfcAWeBfggmNMY%2BuT4Bw9SDJE73i9%2FKE%2BDjseYyIxmSZuo01117MtmQ9xyBne86YOzRfIKpP%2BGTqO2qLKDTcLg3c4wvtnJygY6pgFS8oQc7wz1QGYwVrkTpvEyu%2FbiTuu%2BpPORYsTHQHcci2823hCj7PRaxyALaDnlxtVVCNpqQ845e02aZ%2BoEa3%2BX1yn2foPDHOf6FdU9Kt2Y5B%2FX0kyZRJWbDqblKplrQ%2FBWHsFkwqc7c%2FKrA8VzHZgexZUFfU%2F0OTNai%2Br4AcL3CN4%2Bbvu0tn%2Fq7CTm4v11jyTlpyxEnaclG2%2FUmQFaErloxF3wAl83&X-Amz-Signature=96240a4b04c013150a71a0fbb963bc29ed098c57670c03bb99a47f3f147addc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CC5CRFT%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T123553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGY6NYh253gqlZnUrdne5boX2OE9vYc6UG9L%2B8kX8ZHmAiBJ8zrcxZ4eMoMXD6oyIq5%2BJwNdzDCj0Tsjpwdc0g27hSqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLPzhEfTlPVHDommeKtwDF4liZh%2BzImzOG8Eih7BTdEdLPRFUXjN67UN7%2BUGJ45gd2fT86h%2F0m%2BH%2Bf3M8KAN%2FkaLbR5kPlZ3qyamxz6aZqCx%2B8O5IM9CbQdVVcSXJCtWd48cTYPtI6xEfYuCIPAT5eIYAyQLTjoThUcUrxBoxsCfd3iZlP%2BHupPollzcomPe4qYb2eQihSxUBLrXfLu3njTpqXh%2BGa9dIknrv9wuby7N8im7bKYvglw3S56jjSGkvHzIJ16xs%2FHE8Z%2FpR9asx7fkWR4DyjSprBOMfmmfV%2BOZn0NNQqhxRoW81CmRWHrSnNq3rkFJ5ZX1ODLdTVb5iadHxiUMyjugcn%2F357SeXE%2FbGKI%2FPCNvh5CSV8hd6h7aKGPfivDbhuD8pnqgVuqpKJoMkJXCmaG9w6pSdreJF4gupg12WlvuPmEtyeB%2BARsvRwdkWdRYHWI60LFYTtE3egHGcFBcWWjZ4hXNRnicF%2BMSKLPimQq7t7WKvw1R232nGONcvVn6eVRCatN5pcJNyHWgg4RqUQ4DXxdfzum2fLFUKm47ShT1KFwwfcAWeBfggmNMY%2BuT4Bw9SDJE73i9%2FKE%2BDjseYyIxmSZuo01117MtmQ9xyBne86YOzRfIKpP%2BGTqO2qLKDTcLg3c4wvtnJygY6pgFS8oQc7wz1QGYwVrkTpvEyu%2FbiTuu%2BpPORYsTHQHcci2823hCj7PRaxyALaDnlxtVVCNpqQ845e02aZ%2BoEa3%2BX1yn2foPDHOf6FdU9Kt2Y5B%2FX0kyZRJWbDqblKplrQ%2FBWHsFkwqc7c%2FKrA8VzHZgexZUFfU%2F0OTNai%2Br4AcL3CN4%2Bbvu0tn%2Fq7CTm4v11jyTlpyxEnaclG2%2FUmQFaErloxF3wAl83&X-Amz-Signature=b2ba1340c86b25c7c19b2ddcfa2d668bbcd75e3c0b2f202e10fb134a20c21c55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








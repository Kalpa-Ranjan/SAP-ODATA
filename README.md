



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UF3ATCA%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T134658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJIMEYCIQDjDaLIWt4MjxAv0REh%2FdeYArzPu3RI9ajP0Zjx87TXmQIhAP71crbVjoPfvbpLUE2AF9PsnbZ3I6qLTjTvO6SagMzGKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1JxigH06zL%2Fp2U6Aq3ANk3%2BQxQvK0pAUsiVkaxINSeCOTuHHY%2BKXHcEShKpOaI0TF4REBpxDQpx9RX01KonvIMC7x%2BuCLKcTtIcYd%2BKkW19Rrvx9wdRj5maLyjg2OpPjKa1OS1KAwZlR2%2BrB6UQRVvbkOARuJIYMYS1koVp3%2FfXtMYJbT3w2gcHJ%2Bf1H4eMAs9o0S403l0TO0AO4J38dcNhoTz72Ri%2BENRUqOwwdRjDWO7FFKJea6xK4qcAh2T83%2BhwOxh%2FN8RTyRrbB3z%2FdZ5lsyMkVogGhAQgEEO9fTp2oxYPGp47t6eHWHNJpuO%2Fw2yNsBqR1ulKtG5GFX2xE4ILyp61kJokkYl5bvbHEnFYtY%2BcDw5IRVtvf%2F7jMeUKbRfU8ZKQUdRDvXrMBWP280uilbMiYuTmCUcO8lz1ZggEpULgB0mPU2xh5zb6ckYOoz1TYlD29vBysMhjk15tKJBD5%2BSjqs%2BfoN5xtRTOyMcLzdxAwV63Qmih5bMj41sADhkCA5MftTAIggeZLK3Rwzjc0JaAwNd5iRwt5K5%2Bm7v3%2BuDchlEy5QivsiQDyv5kZJJjukB8szTmcj63dd08YW6apVghXR0msTCAV5etrmxDD37pTUyEkFUeCWcUZA9waC73XebNj8YXU8NTCayJnSBjqkASinsSqib%2BF1Tl4WlOzkJ%2BdqDWktieNsFAafHqfE%2F7fnQs8wmsRbMEW1wAgnpkr5g7G6vmtBtjzINcYH0kiUajGyFWGmtyIvi4Gbdep61e98Tdepkq%2FCw%2BGE4qfUmIXKhrMZ%2F5GvTWyS94xsEQzgd1WVEHtrOcPXhloYReLywzsVF8OX0u50kYbW9BRE1cTszQvkfldioFQUfSbgqPwcwTUgIitf&X-Amz-Signature=5c625e5aa90616aa843083d3e27ef08e8c681f033845b49c30bcc54d6c1b0f45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UF3ATCA%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T134658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJIMEYCIQDjDaLIWt4MjxAv0REh%2FdeYArzPu3RI9ajP0Zjx87TXmQIhAP71crbVjoPfvbpLUE2AF9PsnbZ3I6qLTjTvO6SagMzGKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1JxigH06zL%2Fp2U6Aq3ANk3%2BQxQvK0pAUsiVkaxINSeCOTuHHY%2BKXHcEShKpOaI0TF4REBpxDQpx9RX01KonvIMC7x%2BuCLKcTtIcYd%2BKkW19Rrvx9wdRj5maLyjg2OpPjKa1OS1KAwZlR2%2BrB6UQRVvbkOARuJIYMYS1koVp3%2FfXtMYJbT3w2gcHJ%2Bf1H4eMAs9o0S403l0TO0AO4J38dcNhoTz72Ri%2BENRUqOwwdRjDWO7FFKJea6xK4qcAh2T83%2BhwOxh%2FN8RTyRrbB3z%2FdZ5lsyMkVogGhAQgEEO9fTp2oxYPGp47t6eHWHNJpuO%2Fw2yNsBqR1ulKtG5GFX2xE4ILyp61kJokkYl5bvbHEnFYtY%2BcDw5IRVtvf%2F7jMeUKbRfU8ZKQUdRDvXrMBWP280uilbMiYuTmCUcO8lz1ZggEpULgB0mPU2xh5zb6ckYOoz1TYlD29vBysMhjk15tKJBD5%2BSjqs%2BfoN5xtRTOyMcLzdxAwV63Qmih5bMj41sADhkCA5MftTAIggeZLK3Rwzjc0JaAwNd5iRwt5K5%2Bm7v3%2BuDchlEy5QivsiQDyv5kZJJjukB8szTmcj63dd08YW6apVghXR0msTCAV5etrmxDD37pTUyEkFUeCWcUZA9waC73XebNj8YXU8NTCayJnSBjqkASinsSqib%2BF1Tl4WlOzkJ%2BdqDWktieNsFAafHqfE%2F7fnQs8wmsRbMEW1wAgnpkr5g7G6vmtBtjzINcYH0kiUajGyFWGmtyIvi4Gbdep61e98Tdepkq%2FCw%2BGE4qfUmIXKhrMZ%2F5GvTWyS94xsEQzgd1WVEHtrOcPXhloYReLywzsVF8OX0u50kYbW9BRE1cTszQvkfldioFQUfSbgqPwcwTUgIitf&X-Amz-Signature=356b5335f370fcc2d67f01ccbde77597e7f516b24c2ea1c04579f4e2164c672f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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








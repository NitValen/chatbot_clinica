# chatbot_clinica
  <script>
		function getBotResponse() {
                    i++;
                    var rawText = $("#textInput").val();
                    var userHtml = '<div class="bubbleWrapper"><div class="inlineContainer own"><div class="ownBubble own bg-secondary">'+rawText+ "</div></div></div>"
	            $("#textInput").val("");
	            $("#chatbox").append(userHtml);
                    $.get("/get", { msg: rawText }).done(function (data) {
                      var botHtml = '<div class="bubbleWrapper" id="message'+i+'"><div class="inlineContainer other"><div class="otherBubble other bg-primary">' + data + "</div></div></div>";
	              $("#chatbox").append(botHtml);
	              document
	                  .getElementById("message"+i)
	                  .scrollIntoView({ block: "end", behavior: "smooth" });
                    });
                }
                var i=0;
                $("#textInput").keypress(function (e) {
                    if (e.which == 13) {
                        getBotResponse(i);
                    }
                });
  </script>

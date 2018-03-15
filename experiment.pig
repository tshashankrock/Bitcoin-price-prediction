load_tweets = LOAD '/home/shashank/Desktop/bitcoin/1.json' USING com.twitter.elephantbird.pig.load.JsonLoader('-nestedLoad') AS jsonMap;
data = foreach load_tweets generate jsonMap#'id'           As  tweetid,
                                    jsonMap#'timestamp_ms' As tweetdatatime,
                                    jsonMap#'text'         As tweettext,
				    jsonMap#'retweet_count' As retweetcount
                                    jsonMap#'lang'         As tweetlang,
			            jsonMap#'user'         As tweetuser;
c = FILTER data By ( (chararray)tweetlang == 'en' );
E = FOREACH c GENERATE tweetdatatime, tweettext, tweetlang,retweetcount,tweetuser#'verified' AS usrverified,tweetuser#'follower_count' AS userfollower,tweetuser#'protected' AS userprotected,tweetuser#'statuses_count' AS usrstatus,tweetuser#'friends_count' AS usrfrnds,tweetuser#'protected' AS userprotected,tweetuser#'favourites_count' AS userfavcount,tweetuser#'statuses_count' AS userstatuscount;
dump E;                     

store E into 'json-csvfile' USING org.apache.pig.piggybank.storage.CSVExcelStorage(',','NO_MULTILINE','UNIX','WRITE_OUTPUT_HEADER');

--d = foreach load_tweets generate    jsonMap#'user'   As tweetuser:bag{m:map[]};
--data1 = foreach load_tweets generate tweetuser::m#ID as userid;
--dump data1;
					
--dump c;

--REGISTER elephant-bird-hadoop-compat-4.1.jar;
--REGISTER json-simple-1.1.jar;
--REGISTER elephant-bird-pig-4.1.jar;


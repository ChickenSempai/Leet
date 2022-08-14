class Post {
    public Post(Integer userID, Integer postID, Integer countstamp){
        this.authorID = userID;
        this.postID = postID;
        this.countstamp = countstamp;
    }
    public Integer postID;
    public Integer authorID;
    public Integer countstamp;
}


class Twitter {
    ArrayList<Integer> users;
    HashMap<Integer, HashSet<Integer>> subscribers;
    HashMap<Integer, ArrayList<Post>> feeds;
    HashMap<Integer, ArrayList<Post>> posts;
    Integer postCounter = 0;

    private void init_user_if_new(int userId){
        if (!this.users.contains(userId)){
            this.users.add(userId);
            this.feeds.put(userId, new ArrayList<Post>());
            this.subscribers.put(userId, new HashSet<Integer>());
            this.posts.put(userId, new ArrayList<Post>());
        }
    }

    public Twitter() {
        this.users = new ArrayList<Integer>();
        this.subscribers = new HashMap<Integer, HashSet<Integer>>();
        this.feeds = new HashMap<Integer, ArrayList<Post>>();
        this.posts = new HashMap<Integer, ArrayList<Post>>();
    }

    public void postTweet(int userId, int tweetId) {
        init_user_if_new(userId);
        var post = new Post(userId, tweetId, this.postCounter);
        this.feeds.get(userId).add(post);
        this.posts.get(userId).add(post);
        for(var subscriber: this.subscribers.get(userId).toArray()){
            this.feeds.get(subscriber).add(post);
        }
        ++this.postCounter;
    }

    public List<Integer> getNewsFeed(int userId) {
        init_user_if_new(userId);
        var user_feed = feeds.get(userId);
        var feed_correct_post_order = new ArrayList<Integer>();
        int requested_posts_left = 10;
        for (int i = user_feed.size()-1; i>=0 && requested_posts_left>0; --i){
            feed_correct_post_order.add(user_feed.get(i).postID);
            --requested_posts_left;
        }
        return feed_correct_post_order;
    }


    public void follow(int followerId, int followeeId) {
        init_user_if_new(followerId);
        init_user_if_new(followeeId);
        if (!this.subscribers.get(followeeId).contains(followerId)) {
            this.subscribers.get(followeeId).add(followerId);
            this.insert_followed_posts(this.feeds.get(followerId), this.posts.get(followeeId));
        }
    }

    public void unfollow(int followerId, int followeeId) {
        init_user_if_new(followerId);
        init_user_if_new(followeeId);
        if (this.subscribers.get(followeeId).contains(followerId)) {
            var follower_feed = this.feeds.get(followerId);
            follower_feed.removeIf(post -> (post.authorID == followeeId));
            this.subscribers.get(followeeId).remove(followerId);
        }
    }
    private void insert_followed_posts(ArrayList<Post> follower_feed, ArrayList<Post> followee_posts){
        int insert_index = 0;
        for (var insert_post : followee_posts) {
            while (insert_index < follower_feed.size()
                    && insert_post.countstamp > follower_feed.get(insert_index).countstamp) {
                ++insert_index;
            }
            follower_feed.add(insert_index, insert_post);
        }
    }

}
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post
class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='user1', )

        cls.post1 = Post.objects.create(title='Post Title',
                            text='Post Text',
                            status='pub'
                            ,author =cls.user)
        cls.post2 = Post.objects.create(title='Post Title 2',
                            text='Post Text 2',
                            status=Post.STATUS_CHOICES[1][0]
                            ,author =cls.user)

    def test_post_title(self):
       post = self.post1
       self.assertEqual(str(post), post.title)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.title)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=(self.post1.id,)))
        self.assertEqual(response.status_code, 200)

    def test_status_404_if_post_id_not_found(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)


    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), data={'title':'some title',
                                                                    'text':'some text',
                                                                    'status':'pub',
                                                                    'author':self.user.id})
        self.assertEqual(response.status_code ,302)
        self.assertEqual(Post.objects.last().title, 'some title')
        self.assertEqual(Post.objects.last().text, 'some text')


    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), data={'title':'new title',
                                                                                          'text':'new text',
                                                                                          'status':'pub',
                                                                                        'author':self.post2.author.id})
        self.assertEqual(response.status_code ,302)
        self.assertEqual(Post.objects.last().title, 'new title')
        self.assertEqual(Post.objects.last().text, 'new text')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post1.id]))
        self.assertEqual(response.status_code ,302)

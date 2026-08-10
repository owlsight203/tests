from playwright.sync_api import Page, expect

def test_homepage_load(page: Page):
	page.goto("127.0.0.1:8080")
	body = page.locator("body")
	expect(body).to_be_visible()

	# title = page.title() 

	# assert len(title) > 0

	title = page.locator("h1").first
	expect(title).to_be_visible()


def test_post_detail(page: Page):
	page.goto("127.0.0.1:8080")
	body = page.locator("body")
	expect(body).to_be_visible()

	title_content = page.locator("h5").first
	expect(title_content).to_be_visible()

def test_post_detail_id(page: Page):
	page.goto("127.0.0.1:8080/post/14")
	
	body = page.locator("body")
	expect(body).to_be_visible()

	content_box = page.locator("textarea, input[name='content']").first
	expect(content_box).to_be_visible()

	submit_btn = page.locator("button, input[type='submit']").first
	expect(submit_btn).to_be_visible()
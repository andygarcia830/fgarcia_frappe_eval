frappe.pages['member_profile'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Member Profile',
		single_column: true
	});
}

# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-20 19:52
from __future__ import unicode_literals

from django.db import migrations
import v1.atomic_elements.organisms
import v1.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('regulations3k', '0018_add_notification_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulationlandingpage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([('full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label=b'ID for this content block', required=False))]))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'text', v1.blocks.HeadingTextBlock(required=False)), (b'level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4')])), (b'icon', v1.blocks.HeadingIconBlock(help_text=b'Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#icons">See full list of icons</a>', required=False))], required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'image_width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'full', b'full'), (470, b'470px'), (270, b'270px'), (170, b'170px')])), (b'image_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'right', b'right'), (b'left', b'left')], help_text=b'Does not apply if the image is full-width')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Caption', required=False)), (b'is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'Check to add a horizontal rule line to bottom of inset.', label=b'Has bottom rule line', required=False))])), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'is_large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False)), (b'size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'regular', b'Regular'), (b'large', b'Large Primary')]))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'reusable_text', v1.blocks.ReusableTextChooserBlock(b'v1.ReusableText')), (b'email_signup', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(default=b'Stay informed', required=False)), (b'default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label=b'Default heading style', required=False)), (b'text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), (b'gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label=b'GovDelivery code', required=False)), (b'disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label=b'Privacy Act statement', required=False)), (b'form_field', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Disclaimer', required=False)), (b'inline_info', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Show disclaimer on same line as button. Only select this option if the disclaimer text is a few words (ie, "Privacy Act statement") rather than a full sentence.', label=b'Inline disclaimer', required=False)), (b'label', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')], required=False)), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(required=False))]), icon=b'mail', required=False))])), (b'notification', wagtail.wagtailcore.blocks.StructBlock([(b'message', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Main message of the notification', required=True)), (b'explanation', wagtail.wagtailcore.blocks.TextBlock(help_text=b'An explanation for the notification', required=False)), (b'notification_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'success', b'Success'), (b'warning', b'Warning'), (b'error', b'Error')]))])), (b'regulations_list', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Regulations list heading', required=False)), (b'more_regs_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Link to more regulations')), (b'more_regs_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Text to show on link to more regulations', required=False))]))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='regulationpage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([('info_unit_group', wagtail.wagtailcore.blocks.StructBlock([(b'format', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'50-50', b'50/50'), (b'33-33-33', b'33/33/33'), (b'25-75', b'25/75')], help_text=b'Choose the number and width of info unit columns.', label=b'Format')), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'text', v1.blocks.HeadingTextBlock(required=False)), (b'level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4')])), (b'icon', v1.blocks.HeadingIconBlock(help_text=b'Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#icons">See full list of icons</a>', required=False))], required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'If this field is not empty, the Heading field must also be set.', required=False)), (b'link_image_and_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b"Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'Check this to add a horizontal rule line to top of info unit group.', required=False)), (b'lines_between_items', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'Check this to show horizontal rule lines between info units.', label=b'Show rule lines between items', required=False)), (b'info_units', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'text', v1.blocks.HeadingTextBlock(required=False)), (b'level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4')])), (b'icon', v1.blocks.HeadingIconBlock(help_text=b'Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#icons">See full list of icons</a>', required=False))], default={b'level': b'h3'}, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))]))), (b'sharing', wagtail.wagtailcore.blocks.StructBlock([(b'shareable', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If checked, share links will be included below the items.', label=b'Include sharing links?', required=False)), (b'share_blurb', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', required=False))]))])), ('full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label=b'ID for this content block', required=False))]))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'text', v1.blocks.HeadingTextBlock(required=False)), (b'level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4')])), (b'icon', v1.blocks.HeadingIconBlock(help_text=b'Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#icons">See full list of icons</a>', required=False))], required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'image_width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'full', b'full'), (470, b'470px'), (270, b'270px'), (170, b'170px')])), (b'image_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'right', b'right'), (b'left', b'left')], help_text=b'Does not apply if the image is full-width')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Caption', required=False)), (b'is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'Check to add a horizontal rule line to bottom of inset.', label=b'Has bottom rule line', required=False))])), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'is_large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False)), (b'size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'regular', b'Regular'), (b'large', b'Large Primary')]))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'reusable_text', v1.blocks.ReusableTextChooserBlock(b'v1.ReusableText')), (b'email_signup', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(default=b'Stay informed', required=False)), (b'default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label=b'Default heading style', required=False)), (b'text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), (b'gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label=b'GovDelivery code', required=False)), (b'disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label=b'Privacy Act statement', required=False)), (b'form_field', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Disclaimer', required=False)), (b'inline_info', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Show disclaimer on same line as button. Only select this option if the disclaimer text is a few words (ie, "Privacy Act statement") rather than a full sentence.', label=b'Inline disclaimer', required=False)), (b'label', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')], required=False)), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(required=False))]), icon=b'mail', required=False))])), (b'notification', wagtail.wagtailcore.blocks.StructBlock([(b'message', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Main message of the notification', required=True)), (b'explanation', wagtail.wagtailcore.blocks.TextBlock(help_text=b'An explanation for the notification', required=False)), (b'notification_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'success', b'Success'), (b'warning', b'Warning'), (b'error', b'Error')]))]))]))], blank=True, null=True),
        ),
    ]
